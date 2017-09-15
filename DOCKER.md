
Provided [docker-compose.yml] file does not creates i2pd router CT.
Assume you already have i2pd runing with all needed keys and server tunnels configured.
So to enable access for py-i2phosts to i2p network, you should connect i2pd CT to your newly created network

```
docker network connect pyi2phosts_i2p i2pd
```

```
docker-compose exec app ./manage.py createsuperuser
```
