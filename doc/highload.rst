High-load environments
**********************

Tuning EVA ICS
==============

To use EVA ICS in high-load environments, remember the following:

* Always turn off trace and debug :ref:`logs <config_logs>`. These can
  significantly slows down all EVA ICS components.

* Always check logs. In case of BUS queue overflow, the core may get slower,
  external services may be continuously disconnected. Consider increasing queue
  size in :ref:`config_bus`, increase queue size in services' configuration as
  well (*bus/queue_size*). This helps to cope with high-load peaks.

* Use *buf_ttl_sec* properties of database and replication services to send
  events in bulk. Same (*buf_ttl*) can be used for :ref:`HMI web sockets
  <hmi_ws>`.

* Set *instant_save: false* in :ref:`config_core`.

* If action history is not required, set *keep-action-history* in
  :ref:`config_core` to zero to disable it.

* For slow channels, always use compressed bulk events in :doc:`/svc/eva-repl`.
  Consider using `PSRT <https://psrt.bma.ai/>`_ instead of MQTT, as it is
  designed to cope with slow channel.

* Consider splitting the node and move high-loaded services to other neighbor
  computers.

Hardware
========

Thanks to EVA ICS architecture and optimization for modern multi-core CPUs, the
platform can provide good results even on a microcomputers.

According to tests, EVA ICS can show worse performance on industrial and micro
computers if they have:

* small amount of RAM (minimum 128 MB is recommended)
* slow SSD drive or SD card.

We strongly recommend using at least UHS-I SD cards which can show a speed up
to 100 MB/s. For machines small amount of RAM, consider undeploying all
unnecessary services, including the default ones.
