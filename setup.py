#!/usr/bin/env python

from io import open
from setuptools import setup, find_packages


setup(
    name='django_mobile_auth',
    version='0.2.7',
    packages=find_packages(),
    license='MIT',
    author='Ricardo S. A. Silva',
    description='A Django app that allows users to authenticate using email, phone number or username.',
    keywords='django auth email phone',
    author_email='ricardo@salamandra.cc',
    long_description=open('README.md').read(),
    install_requires=['django', 'django-phonenumber-field==1.3.0', 'phonenumberslite==8.3.2'],
    include_package_data=True,
    url='https://github.com/ricardosasilva/django_mobile_auth',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
