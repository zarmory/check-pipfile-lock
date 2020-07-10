check-pipfile-lock
==================

.. image:: https://img.shields.io/pypi/v/check-pipfile-lock.svg
    :target: https://pypi.python.org/pypi/check-pipfile-lock

.. image:: https://img.shields.io/travis/haizaar/check-pipfile-lock.svg
        :target: https://travis-ci.org/haizaar/check-pipfile-lock

.. image:: https://img.shields.io/pypi/dm/check-pipfile-lock.svg
    :target: https://pypi.python.org/pypi/check-pipfile-lock

This package bridges gab in pipenv tooling by providing
quick and easy way to check whether Pipfile.lock in question
is consistent with the corresponding Pipfile without doing
anything else.

I find it particularly useful with pre-commit hooks (see below)

Usage
-----
::

  check-pipfile-lock <path to Pipfile.lock>

If no path to ``Pipfile.lock`` is provided, the current
directory is assumed.

Pre-commit hook
---------------
Here is the configuration for
`pre-commit <https://pre-commit.com/>`_ framework.

.. code-block:: yaml

  - repo: https://github.com/haizaar/check-pipfile-lock
    rev: v0.0.5
    hooks:
      - id: check-pipfile-lock

Development
-----------
.. code-block:: shell

  echo 'layout pipenv' > .envrc
  direnv allow  # will take a while
  make bootstrap
