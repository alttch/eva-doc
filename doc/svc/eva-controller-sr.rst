Script runner controller
************************

.. contents::

.. include:: /svc_doc/sr.rst


Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-controller-sr.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-controller-sr.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.controller.sr1 /opt/eva4/share/svc-tpl/svc-tpl-controller-sr.yml

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)


EAPI methods
============

See :doc:`/eapi` for the common information about the bus, types, errors and RPC calls.

.. _eva.controller.sr__action:

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

.. _eva.controller.sr__kill:

kill
----

.. list-table::
   :header-rows: 0

   * - Description
     - *Attempts to terinate/cancel all actions for a unit*
   * - Parameters
     - See :ref:`unit_action`
   * - Returns
     - See :ref:`unit_action`

.. _eva.controller.sr__terminate:

terminate
---------

.. list-table::
   :header-rows: 0

   * - Description
     - *Attempts to terminate/cancel a unit action*
   * - Parameters
     - See :ref:`unit_action`
   * - Returns
     - See :ref:`unit_action`

.. _eva.controller.sr__update:

update
------

.. list-table::
   :header-rows: 0

   * - Description
     - *Triggers item update*
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
