Mirror service
**************

.. contents::

Allows to host mirror for the current version of EVA ICS distribution and
Python modules if venv is configured.

Updating mirror files
=====================

Use either :ref:`eva-shell`:

.. code:: shell

  eva mirror update

or :ref:`eva-cloud-manager-cli`:

.. code: shell

  /opt/eva4/bin/eva-cloud-manager node mirror-update


Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-mirror.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-mirror.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.svc.mirror /opt/eva4/share/svc-tpl/svc-tpl-mirror.yml

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)

