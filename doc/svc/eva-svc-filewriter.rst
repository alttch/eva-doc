Item state file writer (JSON/CSV)
*********************************

.. contents::

Allows to write item states into JSON/CSV text files.

The files can be rotated with any external tool or manually. As soon as the
file is rotated, a new one is created automatically.


Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-filewriter.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-filewriter.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.svc.fwriter1 /opt/eva4/share/svc-tpl/svc-tpl-filewriter.yml

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)


EAPI methods
============

See :doc:`/eapi` for the common information about the bus, types, errors and RPC calls.

.. _eva.svc.fwriter__flush:

flush
-----

.. list-table::
   :header-rows: 0

   * - Description
     - *Flushes the output file immediately*
   * - Parameters
     - *none*
   * - Returns
     - *nothing*
