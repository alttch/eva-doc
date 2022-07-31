Connecting to a node
********************

.. contents::

Connection dialog
=================

When Cloud Manager UI is started, the connect window appears automatically:

.. figure:: ss/connect.png
    :scale: 30%

To manage connection, use the marked connect/disconnect tool bar buttons.

Connection path
===============

The following connection modes are supported:

* **http/https** requires :doc:`/svc/eva-hmi` deployed and administrator user
  credentials.

* **rt** connects to a node via the local bus (no credentials required), for
  remote nodes, a bus TCP socket must be configured (see :ref:`config_bus`).

Timeout
=======

The selected timeout must match the longest operating timeout. Consider e.g. if
heavy resource payloads are imported, the timeout must be increased to avoid
errors.
