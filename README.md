# Introduction #

A Django app that allows users to authenticate using email, phone number or username.


## Installation ##


1. Install package:

        pip install django_mobile_auth

2. Add mobile_auth app to INSTALLED_APPS in your django settings.py:

        INSTALLED_APPS = (
            'mobile_auth',
            ...
        )

    Note: Add it before django.contrib.auth if you want to use the custom createsuperuser command with support to email and phone.

3. On you django settings, set the AUTH_USER_MODEL and AUTHENTICATION_BACKENDS to:

    AUTH_USER_MODEL = 'mobile_auth.MobileUser'
    AUTHENTICATION_BACKENDS = ['mobile_auth.backends.MobileAuthBackend',]


## Releases ##

- 0.2.7: Replace fields first_name and last_name with just name. The migration were reset back to 001. Please note before update.
