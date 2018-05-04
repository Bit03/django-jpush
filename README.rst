============
django-jpush
============

-------
Summary
-------
Author: ChainNewsYan
Github: https://github.com/ChainNewsYan/django-jpush
jpush python jiguang 极光 推送 django DRF
This is a package for django.

1. Add "djpush" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'djpush',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^djpush/register', include('djpush.urls.register', namespace='djpush-register')),
    url(r'^djpush/push', include('djpush.urls.push', namespace='djpush-push')),

3. Run `python manage.py migrate` to create the polls models.

--------------------------------------
djpush: django settings require params
--------------------------------------
DEV_KEY = ''
DEV_SECRET = ''
APP_KEY = ''
MASTER_SECRET = ''
