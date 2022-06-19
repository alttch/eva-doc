File manager service
********************

.. contents::

The file manager service allows to remotely deploy/undeploy files to/from
runtime directory. The service is always installed by default, however can
be removed/undeployed for the security purposes without affecting anything
but file deployment.


Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-filemgr.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-filemgr.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.filemgr.main /opt/eva4/share/svc-tpl/svc-tpl-filemgr.yml

or using the bus CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/bus ./var/bus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)


EAPI methods
============

See :doc:`/eapi` for the common information about the bus, types, errors and RPC calls.

.. _eva.filemgr.main__file.get:

file.get
--------

.. list-table::
   :header-rows: 0

   * - Description
     - *Gets a file from runtime directory*
   * - Parameters
     - required
   * - Returns
     - File info or info + content

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **path**
     - String
     - Relative file path
     - **yes**
   * - **mode**
     - String
     - i/x/t/b (info, extended info, text, binary)
     - no
   * - **caller**
     - String
     - m/h (machine/human)
     - no


*Return payload example:*

.. code:: json

  {
      "content_type": "application/x-yaml",
      "modified": 1648693508.311287,
      "path": "test.yml",
      "permissions": 33188,
      "size": 9
  }
  

.. _eva.filemgr.main__file.put:

file.put
--------

.. list-table::
   :header-rows: 0

   * - Description
     - *Puts a file into runtime directory*
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
   * - **path**
     - String
     - Relative file path
     - **yes**
   * - **content**
     - Vec<u8>/String
     - File content
     - **yes**
   * - **permissions**
     - u32/String/bool
     - '0o755' for string, true/false for executable flag
     - no
   * - **sha256**
     - Vec<u8><String>
     - Check sha256 sum of the content before saving
     - no

.. _eva.filemgr.main__file.unlink:

file.unlink
-----------

.. list-table::
   :header-rows: 0

   * - Description
     - *Deletes file from runtime directory*
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
   * - **path**
     - String
     - Relative file path
     - **yes**
