# Django deployment to GCP (Google Cloud Platform) - App Engine
This project contains the following features:
- Settings
- App Engine Deployment
- Database Connection with Postgres

## Settings
To run development environment, you need to use the following command:
``` sh
  python manage.py runserver --settings=DjangoGCPAppEngine.settings.development
```

## App Engine Deployment Files
These files are used for the deployment to GCP - App Engine
- app.yaml
  file to define transfer and configuration to App Engine
- .gcloudignore
  file to define the files and folder to be ignore during deployment to App Engine
- noxfile_config.py
- main.py

## Database connection with Postgres
By default django project is using sqlite. However to deploy GCP App Engine, we need to select a better SQL Engine. GCP providing Postgres database which we can implement by using the following configuration in settings file:

``` py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "/cloudsql/django-project:asia-southeast1:sample-instance",
        "NAME": "database_name_in_here",
        "USER": "user_in_here",
        "PASSWORD": "password_in_here",
    }
}
```

## This code in GitHub does not include the .env file which located inside DjanggoGCPAppEngine (align with wsgi.py, urls.py and asgipy). The sample value of .env file as the following format:

```py
SECRET_KEY= key_is_in_here 
PROD_DEBUG=True
PROD_DB_ENGINE=django.db.backends.postgresql
PROD_DB_HOST=/cloudsql/django-project:asia-southeast1:sample-instance
PROD_DB_NAME=need_to_replace_with_db_name_for_prod
PROD_DB_USERNAME=need_to_replace_with_db_username_for_prod
PROD_DB_PASSWORD=need_to_replace_with_db_password_for_prod
DEV_DEBUG=True
DEV_DB_ENGINE=django.db.backends.postgresql
DEV_DB_IP=123.123.123.123
DEV_DB_NAME=need_to_replace_with_db_name_for_dev
DEV_DB_USERNAME=need_to_replace_with_db_username_for_dev
DEV_DB_PASSWORD=need_to_replace_with_db_password_for_dev
```

## Static and Media File
In this sample code, we still haven't handle static properly to reduce the complexity. 
To handle static and media properly, sample code will be provided in the project DjangoGCPStaticFiles