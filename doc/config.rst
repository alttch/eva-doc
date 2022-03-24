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
additional services. To apply changes, the node server must be restarted.

eva/config/core
---------------

The primary core configuration

.. literalinclude:: ./registry_config/core.yml
    :language: yaml

eva/config/bus
--------------

The node bus configuration

.. literalinclude:: ./registry_config/bus.yml
    :language: yaml

eva/config/registry
-------------------

The built-in registry service configuration

.. literalinclude:: ./registry_config/registry.yml
    :language: yaml

eva/config/logs
---------------

Logging configuration

.. literalinclude:: ./registry_config/logs.yml
    :language: yaml

eva/config/python-venv
----------------------

Configuration of the optional Python virtual environment. To apply changes, it
must be rebuilt with the command:

.. code:: shell

    /opt/eva4/install/build-venv

.. literalinclude:: ./registry_config/python-venv.yml
    :language: yaml

