Installation
************

Preparing the system
====================

The EVA ICS installer prepares the system automatically, installing required
packages. The only necessary pre-installed packages is "curl" to download and
start the installation.

Installing
==========

Basic install
-------------

For a single node, which is going to host a HMI application, type:

.. code:: shell

    curl https://pub.bma.ai/eva/install | sh /dev/stdin -a --hmi

If this is a secondary node and no web services / HTTP API are required, omit
the "--hmi" argument.

.. note::

    As the installer script always installs at least the minimal list of
    required system packages, it must be executed under root.

The installer automatically prepares the system, installs the latest EVA ICS
distribution to /opt/eva4 (default) folder and sets up Python virtual
environment in /opt/eva4/venv (for mode >= 1).

Installer arguments
-------------------

By adding "-h" or "--help" argument, the full list of the installer arguments
can be obtained. Let us review the primary ones:

* **--hmi** automatically setups authentication and web HMI services.

* **--mode** prepares the system, by installing additional packages:

    * **0** installs the minimal list of required packages
    
    * **1** installs Python and eva-shell

    * **2** all of the above, plus C and C++ compilers, plus development headers

    * **3** all of the above, plus Rust compiler and additional development headers

The compilers and the development headers can be used to add custom Python
modules into venv.

* **--prepare-only** allows to install additional compilers / headers, without
  installing EVA ICS. Can be executed after the installation at any time.

Post-install configuration
==========================

Startup and watchdog options can be configured by editing configuration files
in /opt/eva4/etc folder (create them from provided examples if missing).

Additional configuration can be performed by editing :doc:`registry` keys.

.. note::

    The following command:

        EVA_NODE_MODE=registry /opt/eva4/bin/eva-control start

    allows to start the registry database server only

Read more in :doc:`configuring <config>` documentation section.

Startup
=======

If the automatic startup has been set up, EVA ICS node is started automatically
either by Systemd or by OpenRC (Alpine). To start/stop the node server
manually, use either "/opt/eva4/sbin/eva-control" script or
:doc:`eva-shell<cli>`.

Configuring/rebuilding Python venv
==================================

An optional Python virtual environment can be configured using the command:

.. code:: shell

    /opt/eva4/sbin/eva-edit-python-venv

or by editing "eva/config/python-venv" registry key in :doc:`eva-shell<cli>` or
in other tools.

.. code:: shell

    /opt/eva4/install/build-venv

To rebuild the virtual environment from scratch, completely delete
/opt/eva4/venv folder.
