#!/bin/bash -e

fatal()
{
    echo "$@"
    exit 1
}

render_templates()
{
    confd -onetime -backend env
}

# check for mandatory env vars
# we need these vars to fill local_settings.py which used both in `master` and `uwsgi` containers
for var in proxyurl WEBAPPDIR DB_NAME DB_USER DB_PASS DB_HOST TIME_ZONE SECRET_KEY SITE_NAME DOMAIN MY_B64; do
    test "${!var}" || fatal "$var is not set"
done

# default settings
export checker_lookup_retries="${checker_lookup_retries:-1}"
export webappdir="$WEBAPPDIR"
export master_check_interval="${master_check_interval:-43200}"
export master_fetch_interval="${master_fetch_interval:-1800}"
export injector_approve="${injector_approve:-yes}"
export maintainer_external_inactive_max="${maintainer_external_inactive_max:-365}"
export maintainer_internal_inactive_max="${maintainer_internal_inactive_max:-14}"
export maintainer_external_expires="${maintainer_external_expires:-30}"
export maintainer_internal_expires="${maintainer_internal_expires:-30}"
export maintainer_activate_min_delay="${maintainer_activate_min_delay:-3}"
export maintainer_keep_expired="${maintainer_keep_expired:-730}"

# we have 2 modes for this image:
# 1. master: run py-i2phosts-master process
# 2. web-server: run uwsgi and serve requests
case "$1" in
    master) 
        for var in bob_addr builder_hostsfile ; do
            test "${!var}" || fatal "$var is not set"
        done
        render_templates 
        chown -R _pyi2phosts /export
        exec gosu _pyi2phosts py-i2phosts-master -v
        ;;
    uwsgi) 
        # wait for postgres to be ready
        until psql postgres://"$DB_USER:$DB_PASS@$DB_HOST/$DB_NAME" -c '\l'; do
            >&2 echo "Postgres is unavailable - sleeping"
            sleep 1
        done
        ./manage.py collectstatic --noinput
        ./manage.py migrate --noinput
        exec uwsgi --ini uwsgi.ini
        ;;
    *) exec "$@"
esac
