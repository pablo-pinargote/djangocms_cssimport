# djangocms CSS Import plugin

This plugin enables us to reference CSS files directly from the configured static url folder and inject them on the resulting web page on demand.

In the end it allows us to have a clear view at the structure explorer about the components that form part of every section including the css files needed for every one of them.

## Setup

You can install the plugin by:

1. Executing the following command:

```bash
pip install git+https://github.com/pablo-pinargote/djangocms_cssimport
```

2. Adding the plugin to your CMS INSTALLED_APPS settings variable.

```python
INSTALLED_APPS = [
    ### ...,
    'djangocms_cssimport',
]
```

3. Executing plugin migrations to create the corresponding model:

```bash
python manage.py makemigrations djangocms_cssimport
python manage.py migrate djangocms_cssimport
```

## Using the plugin

Using the plugin is very straightforward, we just select it from the plugin's list, and select the file we need to inject.

## Google cloud storage

When the portal is running from Google cloud run it needs to get static files from Google cloud storage; in this case the plugin will try to read the static files using the configured bucket name according to the settings file.

```python
### ...

STATICFILES_STORAGE = 'app.googlestorage.GoogleCloudStaticStorage'

GS_STATIC_BUCKET_NAME = 'my-static-files-bucket-name'

STATIC_URL = f'https://storage.googleapis.com/{GS_STATIC_BUCKET_NAME}/'

### ...
```


