EVA ICS v4 documentation
************************

What is EVA ICS
===============

`EVA ICS <https://www.eva-ics.com>`_ v4 is a new-generation SCADA platform for
Industry-4.0 automated control systems.

* The world-first and only Enterprise SCADA platform, written completely in
  Rust: extremely fast, secure and stable.

* Allows to handle millions of objects on a single node.

* Provides the real control of objects: actions and various automation
  scenarios can be executed, both locally and remotely.

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

.. include:: core_svcs_toc.rst

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

.. toctree::
    :caption: Automation
    :maxdepth: 1

    lmacro/py/python_macros

.. toctree::
    :caption: SDK
    :maxdepth: 1

    eapi
    EVA ICS v4 SDK for Rust <https://crates.io/crates/eva-sdk>
    EVA ICS v4 SDK for Python <https://pypi.org/project/evaics/>
