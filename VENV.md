How to deploy devel environment in virtualenv
=============================================

This file is mostly quick cheat-sheet to myself in case I forgot something.

Install things
--------------

```
git clone
cd py-i2phosts
mkdir venv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Prepare DB, tune local\_settings.py.

Create db structure. In case you need to upgrade from older django versions add `--fake-initial`

```
python manage.py migrate
```

Create superuser to login into admin site (/admin/)

```
./manage.py createsuperuser
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

Collecting static media
-----------------------

```
python ./manage.pycollectstatic
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
