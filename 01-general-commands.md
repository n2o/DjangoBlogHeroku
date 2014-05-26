# General Commands

## Create new project
```bash
python manage.py startapp <name>
```

## Create new app
```bash
python manage.py startapp <name>
```
Then add this app under `settings.py`

## Playing with the API
Starts an interactive shell:
```bash
$ python manage.py shell
```

## Tell South to manage changes to our models
```bash
$ python manage.py schemamigration myapp --initial
$ python manage.py migrate myapp
$ python manage.py schemamigration myapp --auto
```
