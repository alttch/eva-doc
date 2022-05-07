Default ACL service
*******************

.. contents::

Base authorization service, see :doc:`/auth` for more details.

Setup
=====

Use the template *EVA_DIR/share/svc-tpl/svc-tpl-aaa-acl.yml*:

.. literalinclude:: ../svc-tpl/svc-tpl-aaa-acl.yml
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create eva.aaa.acl /opt/eva4/share/svc-tpl/svc-tpl-aaa-acl.yml

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)


EAPI methods
============

See :doc:`/eapi` for the common information about the bus, types, errors and RPC calls.

.. _eva.aaa.acl__acl.deploy:

acl.deploy
----------

.. list-table::
   :header-rows: 0

   * - Description
     - *Deploys ACLs*
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
   * - **acls**
     - Vec<struct>
     - ACLs (same as got in *acl.export*)
     - **yes**

.. _eva.aaa.acl__acl.destroy:

acl.destroy
-----------

.. list-table::
   :header-rows: 0

   * - Description
     - *Destroy a single ACL*
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
     - ACL ID
     - **yes**

.. _eva.aaa.acl__acl.export:

acl.export
----------

.. list-table::
   :header-rows: 0

   * - Description
     - *Export ACLs as a deployment*
   * - Parameters
     - required
   * - Returns
     - ACL deployment struct

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **i**
     - String
     - ACL ID (can be mask)
     - **yes**


*Return payload example:*

.. code:: json

  {
      "acls": [
          {
              "id": "default",
              "meta": {
                  "name": [
                      "default ACL"
                  ]
              },
              "read": {
                  "items": [
                      "#"
                  ]
              },
              "write": {
                  "items": [
                      "#"
                  ]
              }
          }
      ]
  }
  

.. _eva.aaa.acl__acl.format:

acl.format
----------

.. list-table::
   :header-rows: 0

   * - Description
     - *Prepares/combines ACL(s)*
   * - Parameters
     - required
   * - Returns
     - ACL, prepared for authorization

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **i**
     - String/Vec<String>
     - ACL ID or multiple IDs
     - **yes**


*Return payload example:*

.. code:: json

  {
      "admin": true,
      "from": [
          "admin",
          "default"
      ],
      "id": "admin+default",
      "meta": {
          "name": [
              "default ACL"
          ]
      },
      "read": {
          "items": [
              "#"
          ]
      },
      "write": {
          "items": [
              "#"
          ]
      }
  }
  

.. _eva.aaa.acl__acl.get_config:

acl.get_config
--------------

.. list-table::
   :header-rows: 0

   * - Description
     - *Get configuration of a single ACL*
   * - Parameters
     - required
   * - Returns
     - ACL configuration

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **i**
     - String
     - ACL ID
     - **yes**


*Return payload example:*

.. code:: json

  {
      "id": "default",
      "meta": {
          "name": [
              "default ACL"
          ]
      },
      "read": {
          "items": [
              "#"
          ]
      },
      "write": {
          "items": [
              "#"
          ]
      }
  }
  

.. _eva.aaa.acl__acl.list:

acl.list
--------

.. list-table::
   :header-rows: 0

   * - Description
     - *Get list of ACLs and their properties*
   * - Parameters
     - *none*
   * - Returns
     - List of ACLs (struct)


*Return payload example:*

.. code:: json

  [
      {
          "admin": true,
          "id": "admin"
      },
      {
          "id": "default",
          "meta": {
              "name": [
                  "default ACL"
              ]
          },
          "read": {
              "items": [
                  "#"
              ]
          },
          "write": {
              "items": [
                  "#"
              ]
          }
      }
  ]
  

.. _eva.aaa.acl__acl.undeploy:

acl.undeploy
------------

.. list-table::
   :header-rows: 0

   * - Description
     - *Undeploy ACLs*
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
   * - **acls**
     - Vec<struct/String>
     - ACLs or a list of ACL IDs
     - **yes**
