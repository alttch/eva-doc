Modbus slave service
********************

.. contents::

Provides Modbus slave context.

A :doc:`/svc/eva-controller-modbus` can be used later to pull the context
and analyze its data (Modbus via ELBUS is highly recommended).


Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-modbus-slave.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-modbus-slave.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.svc.modbus1 /opt/eva4/share/svc-tpl/svc-tpl-modbus-slave.yml

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)


EAPI methods
============

See :doc:`/eapi` for the common information about the bus, types, errors and RPC calls.

.. _eva.svc.modbus__MB:

MB
--

.. list-table::
   :header-rows: 0

   * - Description
     - *([0x4D 0x42]) Executes Modbus method via ELBUS*
   * - Parameters
     - Modbus request frame, RTU-encoded, unit ID must be 1
   * - Returns
     - Modbus reply frame, RTU-encoded

.. _eva.svc.modbus__save:

save
----

.. list-table::
   :header-rows: 0

   * - Description
     - *Stores Modbus context to disk (if persistent)*
   * - Parameters
     - *none*
   * - Returns
     - *nothing*
