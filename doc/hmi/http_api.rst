.. _hmi_http__login:

login
-----

.. list-table::
   :header-rows: 0

   * - Description
     - *Login and obtain session token (read-write)*
   * - Parameters
     - required
   * - Returns
     - Token information payload

* if no params are given, the method attempts to login user using basic
  auth

* if user and password are set, the method attempts to login user
  using the provided credentials

* if token is set, the method returns token information

* if both user, password and token are set, the method switches the token
  in read-write mode


.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **user**
     - String
     - User login
     - no
   * - **password**
     - String
     - User password (plain)
     - no
   * - **token**
     - String
     - User token
     - no

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/login.req
    :response: http_api_examples/login.resp


.. _hmi_http__logout:

logout
------

.. list-table::
   :header-rows: 0

   * - Description
     - *Ends the user session and destroys the token*
   * - Parameters
     - required
   * - Returns
     - always no error, even if the token does not exist

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **token**
     - String
     - User token
     - **yes**

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/logout.req
    :response: http_api_examples/logout.resp


.. _hmi_http__test:

test
----

.. list-table::
   :header-rows: 0

   * - Description
     - *Tests the node and HMI svc, returns system info*
   * - Parameters
     - required
   * - Returns
     - System info (struct)

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **k**
     - String
     - valid API key
     - **yes**

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/test.req
    :response: http_api_examples/test.resp


