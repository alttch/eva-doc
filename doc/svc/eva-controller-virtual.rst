Virtual controller
******************

.. contents::

The virtual controller service allows to define virtual units and sensors,
which can be used for automation tests, demos and other related purposes.


Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-controller-virtual.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-controller-virtual.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.controller.virtual /opt/eva4/share/svc-tpl/svc-tpl-controller-virtual.yml

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)


EAPI methods
============

See :doc:`/eapi` for the common information about the bus, types, errors and RPC calls.

.. _eva.controller.virtual__action:

action
------

.. list-table::
   :header-rows: 0

   * - Description
     - *Executes a mapped unit action*
   * - Parameters
     - See :ref:`unit_action`
   * - Returns
     - See :ref:`unit_action`

.. _eva.controller.virtual__get:

get
---

.. list-table::
   :header-rows: 0

   * - Description
     - *Gets controller state of a virtual item*
   * - Parameters
     - required
   * - Returns
     - Item state struct

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **i**
     - String
     - Item OID
     - **yes**


*Return payload example:*

.. code:: json

  {
      "oid": "sensor:tests/voltage",
      "status": 1,
      "value": 25.43
  }
  

.. _eva.controller.virtual__list:

list
----

.. list-table::
   :header-rows: 0

   * - Description
     - *Lists virtual items and their states*
   * - Parameters
     - *none*
   * - Returns
     - List (struct)


*Return payload example:*

.. code:: json

  [
      {
          "oid": "unit:tests/door",
          "status": 0,
          "value": null
      },
      {
          "oid": "sensor:tests/temp",
          "status": 1,
          "value": 42.37
      },
      {
          "oid": "sensor:tests/voltage",
          "status": 1,
          "value": 25.43
      }
  ]
  

.. _eva.controller.virtual__set:

set
---

.. list-table::
   :header-rows: 0

   * - Description
     - *Sets controller state of a virtual item*
   * - Parameters
     - required
   * - Returns
     - *nothing*

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **i**
     - String
     - Item OID
     - **yes**
   * - **status**
     - u16
     - Item status
     - no
   * - **value**
     - Any
     - Item state value
     - no
