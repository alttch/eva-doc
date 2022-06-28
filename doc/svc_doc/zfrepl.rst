Zero-failure replication service solves a typical IoT problem, when real-time
data is lost in cases if pub/sub target is offline or a source has temporally
no connection with pub/sub.

The service provides a second replication layer, in addition to
:doc:`/svc/eva-repl`, which 100% guaranties that all telemetry data is
transferred to the target node, unless deleted as expired.

The service is a perfect helper to fill all gaps in logs, charts or any other
kind of archive data representation, collection or analysis.

.. figure:: /schemas/zfrepl.png
    :scale: 100%
    :alt: Zero-failure replication schema

The service can work in 3 modes (only one can be defined in the deployment
config):

Service modes
=============

Collector
---------

Collects real-time data for local :doc:`items </items>` and stores them into
blocks of the subscribed mailboxes. The mailboxes must be called same as the
remote nodes, which collect the data.

The mailbox blocks have compact and crash-free format with serialize+CRC32
scheme, which allows processing all available frames in the block unless a
broken one is detected.

Additionally, telemetry data is know-to-be-compressed-well so it is highly
recommended to compress blocks when transferred (the service client applies
BZIP2-compression automatically).

Additionally, if replication blocks are lost but there is a history database
service on a local node (e.g. :doc:`/svc/eva-db-influx` or
:doc:`/svc/eva-db-sql`), the collector may be asked to fill mailbox with blocks
from the database (see :ref:`eva.zfrepl.N.collector|replicator__mailbox.fill`).

Replicator
----------

Allows to setup mailbox replication, based on a flexible custom schedule (e.g.
every minute, at night only etc.).

Automatically collects replication blocks from remote nodes and pushes them to
the local bus replication archive topic (*ST/RAR/<OID>*).

Requires pub/sub server (`PSRT <psrt.bma.ai/>`_ or `MQTT <https://mqtt.org>`_).
Both source and target node must share same :ref:`api_key`. While being usually
deployed together with :doc:`/svc/eva-repl`, uses a dedicated connection (or a
dedicated server).

Transfers blocks compressed and encrypted.

Standalone
----------

Allows to import manually copied blocks only (see
:ref:`eva.zfrepl.N.collector|replicator__process_dir`).

Recommendations
===============

* Large blocks may cause database service data-flooding on target nodes. Make
  sure these services have enough resources and bus queue size set.

* Keep data blocks small (2-3MB). Approximately, telemetry data is compressed
  10x but the ratio may vary depending on setup.

* If large amount of blocks is generated, increase *block_ttl_sec* mailbox
  collector field.

* `eva.zfrepl.N.collector|replicator__mailbox.fill` may cause significant
  disk/event queue overhead. Make sure the collector service has:

    * enough bus queue
    * enough file ops queue
