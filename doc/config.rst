Configuration
*************

.. contents::

Configuration files
===================

The configuration files are located in */opt/eva4/etc* folder. If the files are
missing, the default values are used.

eva_config
----------

A minimal config, used by "./sbin/eva-control" shell script to start the node
server:

.. literalinclude:: ./etc-config/eva_config-dist
    :language: shell

watchdog_config
---------------

If started in the regular mode, "eva-control" script starts an additional
watchdog shell script, which continuously monitors eva.core and restarts the
node server in case of failures.

.. literalinclude:: ./etc-config/watchdog-dist
    :language: shell

Configuration registry keys
===========================

The configuration registry keys are used by the core to configure itself and
additional services. To apply changes, **the node server must be restarted**:

.. code:: shell

    /opt/eva4/sbin/eva-control restart
    # or using eva-shell
    eva server restart

The keys can be edited with:

.. code:: shell

    /opt/eva4/sbin/eva-registry-cli edit eva/config/X
    # or using eva-shell
    eva edit config/X

.. _config_core:

eva/config/core
---------------

The primary core configuration

.. literalinclude:: ./registry_config/core.yml
    :language: yaml

.. _config_bus:

eva/config/bus
--------------

The node bus configuration

.. literalinclude:: ./registry_config/bus.yml
    :language: yaml

.. _config_registry:

eva/config/registry
-------------------

The built-in registry service configuration

.. literalinclude:: ./registry_config/registry.yml
    :language: yaml

.. _config_logs:

eva/config/logs
---------------

Logging configuration

.. literalinclude:: ./registry_config/logs.yml
    :language: yaml

.. _config_python_venv:

eva/config/python-venv
----------------------

Configuration of the optional Python virtual environment. To apply changes, it
must be rebuilt with the command:

.. code:: shell

    /opt/eva4/sbin/venvmgr build

.. literalinclude:: ./registry_config/python-venv.yml
    :language: yaml

Troubleshooting
===============

If certain parts of the configuration are missing or contain invalid values,
the node may stop starting. Sometimes there may be no messages in logs, e.g. if
the core or the logging system configuration is broken.

In this case, launch the node server in verbose mode with the console output:

.. code:: shell

    /opt/eva/sbin/eva-control launch

Or using :ref:`eva-shell`:

.. code:: shell

    eva server launch

