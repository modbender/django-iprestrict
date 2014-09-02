#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-iprestrict',
    version='0.1.1',
    description='Django app + middleware to restrict access to all or sections of a Django project by client IP ranges',
    long_description='Django app + middleware to restrict access to all or sections of a Django project by client IP ranges',
    author='Tamas Szabo',
    url='https://github.com/sztamas/django-iprestrict',
    download_url='https://github.com/sztamas/django-iprestrict/downloads',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    packages=[
        'iprestrict',
        'iprestrict.management',
        'iprestrict.management.commands',
    ],
    package_data={
        'iprestrict': [
            'templates/iprestrict/*',
            'static/css/*',
            'static/javascript/lib/*',
            'fixtures/*',
            'migrations/*',
        ]
    },
    install_requires=[
        'South==0.7.6',
        'django-templatetag-handlebars==1.2.0',
    ]
)
