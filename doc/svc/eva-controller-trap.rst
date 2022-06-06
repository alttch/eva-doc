SNMP/UDP trap handler
*********************

.. contents::

.. include:: /svc_doc/trap.rst


Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-controller-trap.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-controller-trap.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.controller.trap1 /opt/eva4/share/svc-tpl/svc-tpl-controller-trap.yml

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)

