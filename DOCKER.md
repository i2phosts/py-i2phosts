pyi2phosts in docker
====================

1. Pick [docker-compose.devel.yml](docker-compose.devel.yml) or [docker-compose.prod.yml](docker-compose.prod.yml)
2. Copy it to the docker-compose.yml
3. Adjust enviromment variables inside this file

Development
-----------

```
ln -sf docker-compose.devel.yml docker-compose.yml
docker-compose up --build
```

To run scripts:

```
docker-compose exec app-dev /bin/bash
export PATH=`readlink -ev bin`:$PATH
py-i2phosts-fetcher -c conf-docker/fetcher.conf -d --injector-config conf-devel/injector.conf
py-i2phosts-maint -c conf-docker/maintainer.conf -d
py-i2phosts-checker -d -c conf-docker/checker.conf
```


Production
----------

```
ln -sf docker-compose.prod.yml docker-compose.yml
docker-compose up --build
```


Common docker setup
-------------------

Provided [docker-compose.yml] files does not creates i2pd router CT.
Assume you already have i2pd runing with all needed keys and server tunnels configured.
So to enable access for py-i2phosts to i2p network, you should connect i2pd CT to your newly created network:


```
docker network connect pyi2phosts_default i2pd
```

Create django superuser:

```
docker-compose exec app ./manage.py createsuperuser
```

Clean up:

```
docker network disconnect pyi2phosts_default i2pd
docker-compose down
```
