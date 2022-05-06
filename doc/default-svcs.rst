.. list-table::

   * - Sugg.name
     - Executable
     - Description
     - Install
   * - eva.aaa.acl
     - :doc:`svc/eva-aaa-acl</svc/eva-aaa-acl>`
     - The default ACL service
     - by default in mode 1 (*-a*)
   * - eva.aaa.localauth
     - :doc:`svc/eva-aaa-localauth</svc/eva-aaa-localauth>`
     - Local user/key authentication service
     - by default in mode 1 (*-a*)
   * - eva.controller.enipN
     - :doc:`svc/eva-controller-enip</svc/eva-controller-enip>`
     - Ethernet/IP PLC controller gateway
     - 
   * - eva.controller.modbusN
     - :doc:`svc/eva-controller-modbus</svc/eva-controller-modbus>`
     - Modbus master gateway/service
     - 
   * - eva.controller.py
     - :doc:`venv/bin/eva4-svc-controller-py</svc/eva4-svc-controller-py>`
     - Python macros controller
     - Requires `eva4-controller-py <https://pypi.org/project/eva4-controller-py/>`_ Python module
   * - eva.controller.virtual
     - :doc:`svc/eva-controller-virtual</svc/eva-controller-virtual>`
     - Virtual (test) controller
     - 
   * - eva.db.iN
     - :doc:`svc/eva-db-influx</svc/eva-db-influx>`
     - InfluxDB v1/v2 state history
     - 
   * - eva.db.sN
     - :doc:`svc/eva-db-sql</svc/eva-db-sql>`
     - SQL databases state history
     - 
   * - eva.filemgr.main
     - :doc:`svc/eva-filemgr</svc/eva-filemgr>`
     - File manager service
     - always by default
   * - eva.hmi.default
     - :doc:`svc/eva-hmi</svc/eva-hmi>`
     - HMI (UI) and HTTP API service
     - by default with *--hmi* arg
   * - eva.repl.N
     - :doc:`svc/eva-repl</svc/eva-repl>`
     - replication service
     - 
   * - eva.repl.legacyN
     - :doc:`venv/bin/eva4-svc-repl-legacy</svc/eva4-svc-repl-legacy>`
     - legacy (v3) replication service
     - Requires `eva4-repl-legacy <https://pypi.org/project/eva4-repl-legacy/>`_ Python module
   * - eva.svc.expN
     - :doc:`svc/eva-svc-expiration</svc/eva-svc-expiration>`
     - Item state expiration service
     - 
   * - eva.svc.fwriterN
     - :doc:`svc/eva-svc-filewriter</svc/eva-svc-filewriter>`
     - Item state file writer (JSON/CSV)
     - 
   * - eva.svc.lockerN
     - :doc:`svc/eva-svc-locker</svc/eva-svc-locker>`
     - Shared lock service
     - 
   * - eva.svc.mailer
     - :doc:`svc/eva-svc-mailer</svc/eva-svc-mailer>`
     - Mailer service
     - 
   * - eva.svc.mirror
     - :doc:`svc/eva-svc-mirror</svc/eva-svc-mirror>`
     - EVA ICS / PyPi mirror service
     - 
   * - eva.svc.modbusN
     - :doc:`svc/eva-svc-modbus-slave</svc/eva-svc-modbus-slave>`
     - Modbus slave service
     - 
