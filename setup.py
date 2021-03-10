#!/usr/bin/env python

from os import path
from setuptools import find_packages, setup

from wagtailadminfontawesome import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wagtailadminfontawesome",
    version=__version__,
    description="Add Fontawesome5 to Wagtail project's admin",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Lorenzo",
    # author_email="email@email.com",
    url="https://github.com/lorenzomonte-it/wagtail-admin-fontawesome",
    project_urls={
        'Homepage': 'https://github.com/lorenzomonte-it/wagtail-admin-fontawesome',
    },
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Framework :: Wagtail"
    ],
    install_requires=["Django>=3.1.7", "Wagtail>=2.12.2"],
    zip_safe=False,
)
