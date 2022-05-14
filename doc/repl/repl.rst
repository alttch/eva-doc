The replication service allows V4 nodes to replicate events and interact with
each other.

The nodes must be connected via either `PSRT <https://psrt.bma.ai/>`_ or `MQTT
<https://mqtt.org>`_ pub/sub.

* **PSRT** is an in-house pub/sub protocol, designed especially for industrial
  needs, which can efficiently replicate lots of events per seconds and deal
  with large payloads via slow channels.

* **MQTT** is popular standard IoT protocol, widely used and provided by lots
  of free and commercial service applications, as well as hosted versions from
  various cloud providers.

.. figure:: /schemas/repl.png
    :scale: 80%
    :alt: v4 replication

To communicate, both local and remote node must share the same API key (a key
service is required, e.g. :doc:`/svc/eva-aaa-localauth`. In trusted environment
it is possible to use the same "default" key for all nodes. In untrusted ones
it is recommended to have a dedicated key for each node pair.

.. warning::

    All key fields MUST contain API key ID, not the key value.

The API key specifies ACL(s) for the remote node to handle RPC-via-pub/sub
calls.

To enable all remote bus calls, nodes must also share the same API key with
admin privileges, which must be set in "admin_key" configuration field on the
primary (manager) node. The security policy is the same as for regular keys.

When the "admin_key" is set, the remote node becomes "managed".

.. note::

    Remote bus calls are required for :doc:`/iac` if a deployment configuration
    contains sections for remote nodes.

If discovery is enabled, newly discovered nodes are automatically connected
with the "default_key". Discovery feature is recommended for trusted and
semi-trusted environments.

One node can have multiple replication services deployed. However all of the
must replicate with the own set of remote nodes. Having same remote nodes
replicated by different services leads to abnormal system behavior.
