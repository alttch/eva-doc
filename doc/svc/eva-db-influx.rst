InfluxDB v1/v2 state history
****************************

.. contents::


Use the template *EVA_DIR/share/svc-tpl/None*:

.. literalinclude:: ../svc-tpl/None
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.controller.enip1 /opt/eva4/share/svc-tpl/None

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)

