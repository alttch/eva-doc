SNMP trap handler controller provides easy-to-use way to control SNMP v1/v2c
traps.

Processing
==========

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
=========================

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
