FROM python:2

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1
ENV WEBAPPDIR=/opt/py-i2phosts

# install gosu https://github.com/tianon/gosu/blob/master/INSTALL.md
ENV GOSU_VERSION 1.10
ENV CONFD_VERSION 0.13.0
RUN set -ex; \
    \
    fetchDeps=' \
        ca-certificates \
        wget \
    '; \
    apt-get update; \
    apt-get install -y --no-install-recommends $fetchDeps; \
    \
    dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
    wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
    chmod +x /usr/local/bin/gosu; \
# verify that the binary works
    gosu nobody true; \
    \
# install confd here too
    wget -O /usr/local/bin/confd https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-linux-amd64 ;\
    chmod +x /usr/local/bin/confd; \

# install needed packages
    apt-get install -y --no-install-recommends postgresql-client netcat ;\

    rm -rf /var/lib/apt/lists/*; \
    apt-get purge -y --auto-remove $fetchDeps

# copy our reqs
COPY requirements.txt $WEBAPPDIR/

# install uwsgi and deps
RUN pip install --no-cache-dir uwsgi && \
    pip install --no-cache-dir -r $WEBAPPDIR/requirements.txt && \
    useradd -d $WEBAPPDIR -M _pyi2phosts && \
    mkdir -p /etc/py-i2phosts/

# py-i2phosts config templates
COPY docker/confd/templates/* /etc/confd/templates/
COPY docker/confd/toml/* /etc/confd/conf.d/

# uwsgi config
COPY docker/uwsgi.ini $WEBAPPDIR/

# copy our files
COPY bin/* docker/docker-entrypoint.sh /usr/local/bin/
COPY manage.py $WEBAPPDIR/
COPY pyi2phosts/ $WEBAPPDIR/pyi2phosts/

# local_settings
COPY docker/local_settings.py $WEBAPPDIR/pyi2phosts/

# volume for generated hosts.txt
#VOLUME /export
# volume for static media
#VOLUME /static

ENV builder_hostsfile /export/alive-hosts.txt

# set workdir to later launch stuff from it
WORKDIR $WEBAPPDIR

ENTRYPOINT ["docker-entrypoint.sh"]
