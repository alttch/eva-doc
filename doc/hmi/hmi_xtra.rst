HTTP API
========

Basics
------

HTTP API requests are performed using `JSON RPC 2.0
<https://www.jsonrpc.org/specification>`.

If JSON RPC request is called without ID, it means that the server does not
need to return a result. In this case, http response with a code *202
Accepted* is returned.

JSON RPC API URL:

    **\http://<IP/DOMAIN[:SVC_LISTEN_PORT]>/jrpc**

    or

    **\http://<IP/DOMAIN[:SVC_LISTEN_PORT]>/**

    (all POST requests to the root URI are processed as JSON RPC)

JSON RPC payload encoding
~~~~~~~~~~~~~~~~~~~~~~~~~

Supported encodings are generic JSON and as `MessagePack
<https://msgpack.org/>`_.

To call API methods with MessagePack-encoded payloads, use *Content-Type:
application/msgpack* HTTP request header.

JSON RPC error responses
~~~~~~~~~~~~~~~~~~~~~~~~

Response field *"message"* may contain additional information about error.

.. warning::

    It is highly not recommended to perform long API calls, calling API
    functions from JavaScript in a web browser (e.g. giving "w" param to action
    methods to wait until action finish). The web browser may repeat API call
    continuously considering them as timed-out, which leads to absolutely
    unexpected behavior.

JSON RPC via HTTP GET
~~~~~~~~~~~~~~~~~~~~~

Embedded equipment sometimes can send HTTP GET requests only. JSON RPC API
supports such calls as well.

To make JSON RPC API request with HTTP get, send it to:

    **\http://<IP/DOMAIN>[:SVC_LISTEN_PORT]/jrpc?i=ID&m=METHOD&p=PARAMS**

where:

* **ID** request ID (any custom value). If not specified, API response isn't
  sent back
* **METHOD** JSON RPC method to call
* **PARAMS** method params, as url-encoded JSON

E.g. the following HTTP GET request will invoke method "test" with request id=1
and params *{ "k": "mykey" }*:

    *\http://localhost:7727/jrpc?i=1&m=test&p=%7B%22k%22%3A%22mykey%22%7D*

.. note::

    JSON RPC API calls via HTTP GET are insecure, limited to 2048 bytes and can
    not be batch. Use JSON RPC via HTTP POST with JSON or MessagePack payload
    always when possible.



Web socket methods
==================

Web socket method can be executed using a web socket, connected to:

    **ws://<IP/DOMAIN>[:SVC_LISTEN_PORT]/ws**

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
