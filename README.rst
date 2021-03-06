Course Discovery Service  |Travis|_ |Codecov|_
==============================================
.. |Travis| image:: https://travis-ci.org/edx/course-discovery.svg?branch=master
.. _Travis: https://travis-ci.org/edx/course-discovery

.. |Codecov| image:: http://codecov.io/github/edx/course-discovery/coverage.svg?branch=master
.. _Codecov: http://codecov.io/github/edx/course-discovery?branch=master

Service providing access to consolidated course and program metadata.

Documentation
-------------

`Documentation <https://edx-discovery.readthedocs.io/en/latest/>`_ is hosted on Read the Docs. The source is hosted in this repo's `docs <https://github.com/edx/course-discovery/tree/master/docs>`_ directory. The docs are automatically rebuilt and redeployed when commits are merged to master. To contribute, please open a PR against this repo.

License
-------

The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. Please see the LICENSE_ file for details.

.. _LICENSE: https://github.com/edx/course-discovery/blob/master/LICENSE

How To Contribute
-----------------

Contributions are welcome. Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details. Even though it was written with ``edx-platform`` in mind, these guidelines should be followed for Open edX code in general.

Development
-----------

Is the build failing because translations are out of date?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Run ``make check_translations_up_to_date`` and check in the generated *.mo & *.po files to your PR.

Running Tests Locally, Fast
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a test settings file ``course_discovery.settings.test_local`` that allows you to persist the test
database between runs of the unittests (as long as you don't restart your container).  It stores the SQLite
database file at ``/dev/shm``, which is a filesystem backed by RAM.  Using this test file in conjunction with
pytest's ``--reuse-db`` option can significantly cut down on local testing iteration time.  You can use this
as follows: ``pytest course_discovery/apps/course_metadata/tests/test_utils.py --ds=course_discovery.settings.test_local --reuse-db``

The first run will incur the normal cost of database creation (typically around 30 seconds), but the second run
will completely skip that startup cost, since the ``--reuse-db`` option causes pytest to use the already persisted
database in the ``/dev/shm`` directory.  If you need to change models or create databases between runs, you can tell
pytest to recreate the database with ``-recreate-db``.


Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Get Help
--------

Ask questions and discuss this project on `Slack <https://openedx.slack.com/messages/general/>`_ or in the `edx-code Google Group <https://groups.google.com/forum/#!forum/edx-code>`_.
