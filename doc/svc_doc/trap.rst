SNMP/UDP trap handler controller provides easy-to-use way to process SNMP
v1/v2c and EVA ICS native UDP traps.

SNMP Traps
==========

Processing
----------

A trap data is parsed and processed later with a custom :ref:`lmacro` with the
following keyword arguments:

==============  ================  ==================================
Name            Type              Content
==============  ================  ==================================
trap_source     String            SNMP trap sender IP address
trap_community  String            SNMP trap community
trap_vars       Map<String, Any>  Trap variables map as SNMP_OID=VAL
==============  ================  ==================================

Supported SNMP data types
-------------------------

The following SNMP data types are parsed and sent in *trap_vars*:

===========  ===================
Type         Processed as
===========  ===================
BER (X.690)  u64/i64/bool/String
Counter32    u32
Gauge32      u32
UInteger32   u32
Counter64    u64
String       String
===========  ===================

Unsupported data types are ignored.

Native traps
============

EVA ICS native traps is a native UDP signaling trap protocol, which replaces v3
UC UDP API.

The native trap structure is a string with new-line (LF) separated commands,
e.g.:

.. code::

    u sensor:env/temp 1 25.57
    a unit:tests/motor1 1 34.22
    a unit:tests/relay1 toggle

.. note::

    Native traps are processed by the service directly, the process macro is
    not required to be set.

Updates
-------

Update commands have the following format:

.. code::

    u[pdate] <OID> <status> [value]

Example:

.. code::

    u sensor:env/temp 1 25.57

Actions
-------

Action commands have the following format:

.. code::

    a[action] <OID> <status> [value]

Example:

.. code::

    a unit:tests/motor1 1 34.22

If a toggle-action is required to be executed, use "t" (or "toggle") as the
status.
