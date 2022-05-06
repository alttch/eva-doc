.. list-table::

   * - Suggested name
     - Executable
     - Description
     - Install
   * - :doc:`eva.aaa.acl</svc/eva-aaa-acl>`
     - svc/eva-aaa-acl
     - :doc:`The default ACL service</svc/eva-aaa-acl>`
     - by default with HMI (*--hmi*)
   * - :doc:`eva.aaa.localauth</svc/eva-aaa-localauth>`
     - svc/eva-aaa-localauth
     - :doc:`Local user/key authentication service</svc/eva-aaa-localauth>`
     - by default with HMI (*--hmi*)
   * - :doc:`eva.controller.enipN</svc/eva-controller-enip>`
     - svc/eva-controller-enip
     - :doc:`Ethernet/IP PLC controller gateway</svc/eva-controller-enip>`
     - 
   * - :doc:`eva.controller.modbusN</svc/eva-controller-modbus>`
     - svc/eva-controller-modbus
     - :doc:`Modbus master gateway/service</svc/eva-controller-modbus>`
     - 
   * - :doc:`eva.controller.py</svc/eva4-svc-controller-py>`
     - venv/bin/eva4-svc-controller-py
     - :doc:`Python macros controller</svc/eva4-svc-controller-py>`
     - Requires `eva4-controller-py <https://pypi.org/project/eva4-controller-py/>`_ Python module
   * - :doc:`eva.controller.virtual</svc/eva-controller-virtual>`
     - svc/eva-controller-virtual
     - :doc:`Virtual (test) controller</svc/eva-controller-virtual>`
     - 
   * - :doc:`eva.db.iN</svc/eva-db-influx>`
     - svc/eva-db-influx
     - :doc:`InfluxDB v1/v2 state history</svc/eva-db-influx>`
     - 
   * - :doc:`eva.db.sN</svc/eva-db-sql>`
     - svc/eva-db-sql
     - :doc:`SQL databases state history</svc/eva-db-sql>`
     - 
   * - :doc:`eva.filemgr.main</svc/eva-filemgr>`
     - svc/eva-filemgr
     - :doc:`File manager service</svc/eva-filemgr>`
     - always by default
   * - :doc:`eva.hmi.default</svc/eva-hmi>`
     - svc/eva-hmi
     - :doc:`HMI (UI) and HTTP API service</svc/eva-hmi>`
     - by default with *--hmi* arg
   * - :doc:`eva.repl.N</svc/eva-repl>`
     - svc/eva-repl
     - :doc:`replication service</svc/eva-repl>`
     - 
   * - :doc:`eva.repl.legacyN</svc/eva4-svc-repl-legacy>`
     - venv/bin/eva4-svc-repl-legacy
     - :doc:`legacy (v3) replication service</svc/eva4-svc-repl-legacy>`
     - Requires `eva4-repl-legacy <https://pypi.org/project/eva4-repl-legacy/>`_ Python module
   * - :doc:`eva.svc.expN</svc/eva-svc-expiration>`
     - svc/eva-svc-expiration
     - :doc:`Item state expiration service</svc/eva-svc-expiration>`
     - 
   * - :doc:`eva.svc.fwriterN</svc/eva-svc-filewriter>`
     - svc/eva-svc-filewriter
     - :doc:`Item state file writer (JSON/CSV)</svc/eva-svc-filewriter>`
     - 
   * - :doc:`eva.svc.lockerN</svc/eva-svc-locker>`
     - svc/eva-svc-locker
     - :doc:`Shared lock service</svc/eva-svc-locker>`
     - 
   * - :doc:`eva.svc.mailer</svc/eva-svc-mailer>`
     - svc/eva-svc-mailer
     - :doc:`Mailer service</svc/eva-svc-mailer>`
     - 
   * - :doc:`eva.svc.mirror</svc/eva-svc-mirror>`
     - svc/eva-svc-mirror
     - :doc:`EVA ICS / PyPi mirror service</svc/eva-svc-mirror>`
     - 
   * - :doc:`eva.svc.modbusN</svc/eva-svc-modbus-slave>`
     - svc/eva-svc-modbus-slave
     - :doc:`Modbus slave service</svc/eva-svc-modbus-slave>`
     - 
