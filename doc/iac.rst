IaC and deployment
******************

EVA ICS supports infrastructure-as-code paradigm, providing a way to deploy
resources and their parameters from deployment files in YAML format.

.. note::

    To allow deployment on remote nodes, the local node must have remotes
    connected in management mode (the :doc:`replication service
    </svc/eva-repl>` field "admin_key" must be set).

.. contents::

Deployment file
===============

Deployment configurations are stored in YAML files, which have the following
format:

.. code:: yaml

    version: 4
    content:
        - node: <NODE_NAME>
        # ......
        - node: <NODE_NAME>
        # ......

An alias ".local" can be used for the local node deployment.

AAA
---

:doc:`User account, API keys and ACLs </aaa>` can be deployed as well, per
node. Note that user passwords contain password hashes, not the passwords
itself. The hash can be get using e.g. Linux shell command:

.. code:: shell

    echo -n PASSWORD|sha256sum

.. code:: yaml

    - node: .local
      acls:
        - id: admin2
          admin: true
        - id: default2
          read:
            items:
              - "#"
          write:
            items:
              - "#"
          meta:
              name:
                - "default ACL #"
      keys:
        - id: admin2
          key: "mykey2"
          acls:
            - admin2
      users:
        - login: admin2
          password: cd2eb0837c9b4c962c22d2ff8b5441b7b45805887f051d39bf133b583baf6860
          acls:
            - admin2

Uploading files
---------------

Local files can be uploaded to the target's EVA_DIR/runtime directory with the
following block:

.. code:: yaml

    - node: .local
      upload:
        - src: deploy.info
          target: data/
          # override the file permissions, specify in oct
          permissions: 0o400
        - src: xx.yml
          target: data/x.yml
          svc: eva.filemgr.main # override the file manager
        - text: |
            hello, i am here
          target: data/some-file

.. note::

    If a file content is defined directly in the deployment (field *text*), the
    target MUST contain the full destination path, including the file name.

The upload source field accepts both local files and HTTP URLs.

Items
-----

:doc:`/items` can be deployed in "items" section:

.. code:: yaml

    - node: .local
      items:
        - oid: unit:tests/door
          status: 1
          action:
            svc: eva.controller.virtual
        - oid: unit:tests/door2
          enabled: true

Units, sensors and lvars can contain initial status and value fields. The
fields are ignored if items already exist and the current states are kept.

Macros
------

:ref:`lmacro` are deployed as all other items. If
:doc:`/lmacro/py/python_macros` are used, upload the macro code to *xc/py*
subdirectory of the target's runtime:

.. code:: yaml

    - node: .local
      upload:
        - src: m1.py
          target: xc/py/m1.py
      items:
        - oid: lmacro:tests/m1
          action:
            svc: eva.controller.py

Services
--------

It is possible to deploy new services on the target. After the node is
deployed, the deployment process waits until all deployed services are started
before continue.

.. code:: yaml

    - node: .local
      svcs:
        - id: eva.svc.locker2
          params:
            bus:
              path: var/elbus.ipc
            command: svc/eva-svc-locker
            config:
              locks:
                - lock1
                - lock2
                - lock3
            workers: 1
            user: nobody
 
Extra commands
--------------

BUS calls
~~~~~~~~~

Node bus calls can be automatically executed before/after the deployment is
complete:

.. code:: yaml

    - node: .local
      extra:
        deploy:
          before:
            - method: test
            - method: item.list
              params:
                i: '#'
            - method: eva.registry::server_set
              params:
                name: auto_flush
                value: false
          after:
            - method: eva.registry::server_set
              params:
                name: auto_flush
                value: true
        undeploy:
          before:
            - method: svc.purge
              params:
                svcs:
                  - eva.svc.locker2
              _pass: true

API calls are always executed in the specified order, one-by-one, *method:*
field contains EAPI method function to execute. The default target is :doc:`the
target node core </core>`, to specify a service call, use the format
"TARGET_SVC::METHOD".

The special parameter *_pass* allows to ignore errors.

Additional deploy functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

sleep
^^^^^

Delays execution of next before/after deploy commands. E.g. the following block
makes 1-sec delay after undeployment:

.. code:: yaml

    - node: .local
      extra:
        undeploy:
          after:
            - function: sleep
              args: [ 1 ]

system
^^^^^^

Executes (local) system command:

.. code:: yaml

    - node: .local
      extra:
        undeploy:
          after:
            - function: system
              args: [ "touch /tmp/xxx.flag" ]

Deployment via CLI
==================

Deploying
---------

Deployment configuration can be applied using  *eva cloud deploy* (or
*eva-cloud-manager cloud deploy*) command.  When deployed with
:doc:`CLI</cli>`, deployment files can contain external variables.

Example:

.. code:: yaml

    - node: {{ srv }}
      items:
        - oid: sensor:{{ srv }}/env/temp

Here is *srv* variable defined. To set its value, e.g. to "plant1", use *-c
srv=plant* command line argument. If multiple variable values are going to be
set, use *-c* argument multiple times.

The default deployment timeout is 5 seconds. If some deployment calls
require more time to be executed, consider increasing the timeout value
with command-line argument *-T*:

.. code:: shell

    eva -T 15 cloud deploy file.yml

The deployment file can be a local one or HTTP URL.

If :doc:`/registry` auto-flush is enabled on the target and multiple items are
deployed, the deployment may take long time to complete. The registry
auto-flush can be automatically switched off and back on with the following
block:

.. code:: yaml

    - node: .local
      extra:
        deploy:
          after:
          - method: eva.registry::server_set
            params:
              name: auto_flush
              value: true
          before:
          - method: eva.registry::server_set
            params:
              name: auto_flush
              value: false
        undeploy:
          after:
          - method: eva.registry::safe_purge
          - method: eva.registry::server_set
            params:
              name: auto_flush
              value: true
          before:
          - method: eva.registry::server_set
            params:
              name: auto_flush
              value: false

The block also calls safe_purge to cleanup the registry after undeploy.

Undeploying
-----------

Deployment configuration can be removed with *eva cloud undeploy*
(*eva-cloud-manager cloud undeploy*) command.  Custom variable values can be
set in the same way as during deployment.

Advanced configuration
======================

:ref:`yaml_advanced` directives are processed by the deployment CLI tool on the
local machine. If the target deployment (e.g. a service configuration) must
contain these directives, use "^^" directive prefix instead of a single one.
