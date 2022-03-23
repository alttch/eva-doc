Command-line tools
******************

eva-shell
=========

The primary command-line tool to manage EVA ICS nodes is **eva-shell**, which
is either :doc:`installed <install>` automatically or can be added later, by
including "eva-shell" Python module in the Python virtual environment.

.. figure:: eva-shell.png
    :scale: 50%
    :alt: eva-shell

    with eva-shell, IoT management is a joy

EVA ICS v4 eva-shell can work in both command-line and interactive mode (type
"eva" without arguments to start it).

The interactive mode provides various features, like TAB-auto-completion,
command repetitions ("command \|T" or "command \|cT", where T is the command
interval, in seconds) etc.

ELBUS CLI
=========

Various calls to the EVA ICS core and services can be performed with
"sbin/elbus" command-line tool.

.. note::

    EVA ICS ELBUS RPC uses MessagePack-packed payloads. To convert YAML to
    MessagePack, a tool "bin/yml2mp" is provided.

Registry management
===================

* **bin/eva-registry** registry interactive/command-line tool (Python, installed
  automatically with eva-shell)

* **sbin/eva-registry-cli** registry command-line tool (included by default)

* **sbin/key-as-source** and **sbin/key-set-flag** wrappers around
  "eva-registry-cli" for certain tasks.
