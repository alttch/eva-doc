EVA ICS v4 documentation
************************

What is EVA ICS
===============

`EVA ICS <https://www.eva-ics.com>`_ v4 is a new-generation SCADA platform for
Industry-4.0 automated control systems.

* The world-first and only Enterprise SCADA platform, written completely in
  Rust: extremely fast, secure and stable.

* Allows to handle millions of objects on a single node.

* Provides the real control of objects, instead of just monitoring, objects can
  receive and perform actions.

* The new v4 micro-kernel architecture is completely scalable and allows to
  build complex setups for any industrial needs: factories, power plants,
  military sector etc.

* Real-time event replication between cluster nodes and web HMI applications.

* Supported architectures out-of-the-box (Linux only): x86_64, ARMv7, AARCH64

.. note::

    This is the primary EVA ICS documentation site. For troubleshooting,
    firstly check the `EVA ICS Knowledge base <https://kb.eva-ics.com/>`_.

.. toctree::
    :caption: System documentation
    :maxdepth: 1

    install
    What is new <changelog>
    architecture
    config
    registry
    items
    auth
    cli
    highload
    enterprise
    trademarks

.. toctree::
    :caption: Services
    :maxdepth: 1

    core
    svc/aaa-acl
    svc/aaa-localauth
    svc/db-influx
    svc/db-sql
    svc/expiration
    svc/hmi
    svc/replication-legacy

.. toctree::
    :caption:  Interface development
    :maxdepth: 1

    ui
    pvt
    serve_as
    upload
    api_tokens
    evahi
    EVA JS Framework <https://github.com/alttch/eva-js-framework>
