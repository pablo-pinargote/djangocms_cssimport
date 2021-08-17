# djangocms CSS Import plugin

This plugin enables us to reference CSS files directly from the static url folder and inject them on the resulting web page on demand and from within the structure explorer.

In the end it allows us to have a clear view at structure explorer about the components that form part of every section.

## Setup

You can install the plugin by:

1. Executing the following command:

```bash
pip install git+https://github.com/pablo-pinargote/djangocms_cssimport
```

2. Adding the plugin to your CMS INSTALLED_APPS settings variable.

```python
INSTALLED_APPS = [
    ...,
    'djangocms_cssimport',
]
```

3. Executing plugin migrations to create the corresponding model:

```bash
python manage.py makemigrations djangocms_cssimport
python manage.py migrate djangocms_cssimport
```

## Using the plugin

Using the plugin is very straightforward, we just select it from the plugin's list, enter a label (optional) and the path to the css file.
