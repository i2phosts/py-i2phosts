How to deploy devel environment in virtualenv
=============================================

```
git clone
cd py-i2phosts
mkdir venv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

In case you need to upgrade from older django versions:

```
python manage.py migrate --fake-initial
```

Running django
--------------

```
python manage.py runserver
```

Running scripts
---------------

```
export PATH=$PATH:`readlink -ev bin`
py-i2phosts-fetcher -c conf-devel/fetcher.conf -d --injector-config conf-devel/injector.conf
py-i2phosts-maint -c conf-devel/maintainer.conf -d
py-i2phosts-checker -d -c conf-devel/checker.conf
```

Updating locale messages
------------------------

```
cd pyi2phosts
django-admin makemessages
```

Create migrations after updating models
---------------------------------------

```
python ./manage.py makemigrations
```
