#!/usr/bin/env python

from setuptools import setup

with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="check-pipfile-lock",
    version="0.0.1",
    description="Check pipenv's Pipfile.lock to be consistent with Pipfile",
    long_description=readme,
    author="Zaar Hai",
    author_email="haizaar@haizaar.com",
    url="https://github.com/haizaar/check-pipfile-lock",
    license=license,
    packages=["."],
    install_requires=("click", "clickclick", "pipenv"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ("check-pipfile-lock=check_pipfile_lock:main",)},
)
