EVA ICS v4 documentation
************************

What is EVA ICS
===============

`EVA ICS <https://www.eva-ics.com>`_ v4 is a new-generation Industrial-IoT
SCADA platform for Industry-4.0 automated control systems.

* The world-first and only Enterprise SCADA platform, written completely in
  Rust: extremely fast, secure and stable.

* Allows to handle millions of objects on a single node.

* Provides the real control of objects: actions and various automation
  scenarios can be executed, both locally and remotely.

* The new v4 micro-kernel architecture is completely scalable and allows to
  build complex setups for any industrial needs: factories, power plants,
  military sector etc.

* Real-time event :doc:`replication</svc/eva-repl>` and interaction between
  cluster nodes and web HMI applications.

* Supported architectures out-of-the-box (Linux only): x86_64, aarch64.

.. note::

    This is the primary EVA ICS documentation site. For troubleshooting,
    firstly check the `EVA ICS Knowledge base <https://kb.eva-ics.com/>`_.

.. toctree::
    :caption: System documentation
    :maxdepth: 1

    install
    v3migration
    What is new <changelog>
    architecture
    config
    registry
    aaa
    items
    cli
    iac
    highload
    enterprise

.. include:: core_svcs_toc.rst

.. toctree::
    :caption:  Interface development
    :maxdepth: 1

    ui
    hmi/pvt
    hmi/serve_as
    hmi/upload
    hmi/server_templates
    hmi/frontend
    EVA JS Framework <https://github.com/alttch/eva-js-framework>

.. toctree::
    :caption: Automation
    :maxdepth: 1

    auto/invert
    svc/eva-controller-lm
    lmacro/py/python_macros

.. toctree::
    :caption: SDK
    :maxdepth: 1

    eapi
    EVA ICS v4 SDK for Rust <https://crates.io/crates/eva-sdk>
    EVA ICS v4 SDK for Python <https://pypi.org/project/evaics/>
    /repl/proto

.. toctree::
    :caption: Legal
    :maxdepth: 1

    License <https://github.com/alttch/eva4/blob/master/LICENSE>
    trademarks
