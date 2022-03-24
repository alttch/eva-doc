Serving structured data
***********************

.. contents::

Structured data (YAML and JSON files) is very typical for UI development to
keep settings, texts and other structured information.

EVA ICS default HMI service provides a feature, called "serve as", which allows
to convert any structured data file on-the-flow and load it into UI
applications in the most convenient way.

This feature is supported by both public UI ("/ui" URLs) and :doc:`pvt` and
enabled automatically for all YAML and JSON files.

.. _serve_as_format:

Format conversion
=================

To convert a structured file into another format, request it as:

    /ui/filename.yml?as=FMT

where FMT:

* **yml** (or yaml) - convert the file into YAML
* **json** - convert the file into JSON
* **js** - convert the file into JavaScript (requires either "var" or "func" as
  the additional parameter)

e.g. let's convert YAML, which is usually more human-editable and preferred to
keep configs, into JSON:

    /ui/filename.yml?as=json

The file can also be converted on-the-flow to JavaScript variable, or, as
copying JavaScript arrays and dicts is usually tricky, into the function, which
returns the structured data on every call:

    /ui/filename.yml?as=js&func=myfunc

Serving structured data from EVA ICS Registry
=============================================

To serve structured data from :doc:`EVA ICS registry<registry>`, use the
following request:

.. code-block:: bash

    http://<IP:7727>/:pub/REGISTRY-KEY

where REGISTRY-KEY - key name, relative to *eva/user_data/pub*, e.g.
to request a key "eva/user_data/pub/settings" use the following request:

.. code-block:: bash

    http://<IP:7727>/:pub/settings

By default, registry data is served in JSON. To change format or add locale
translation, see :ref:`serve_as_format` and :ref:`serve_as_locale`.

To serve private data, see :ref:`pvt_registry`.

Why serving structure data from the registry is more convenient than using
files:

* reliability
* unified data storage
* data schemas
