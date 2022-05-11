Web socket methods
==================

Web socket method can be executed using a web socket, connected to:

    ws://<IP/DOMAIN>[:SVC_LISTEN_PORT]/ws

Web socket methods provide one-way RPC calls with no returns. If a method
returns a value it means that the value is "ordered" and can be returned any
time when processed.

The web socket RPC payload MUST be JSON-encoded and contains the following
fields:

.. list-table::
   :header-rows: 0

   * - Field
     - Type
     - Description
     - Required
   * - method
     - String
     - method name
     - **yes**
   * - params
     - Any
     - parameters
     - no

Example:

.. code:: json

    {
        "method": "subscribe.state",
        "params": ["#"]
    }

.. include:: /hmi/ws_api.rst
