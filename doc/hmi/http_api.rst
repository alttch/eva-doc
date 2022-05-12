.. _hmi_http__item.state:

item.state
----------

.. list-table::
   :header-rows: 0

   * - Description
     - *Gets state of item(s)*
   * - Parameters
     - required
   * - Returns
     - List of item states

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **k**
     - String
     - valid API key/token
     - **yes**
   * - **i**
     - Vec<String>/String
     - Item OID(s) or masks
     - no
   * - **full**
     - bool
     - Full state (enabled + meta)
     - no

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/item.state.req
    :response: http_api_examples/item.state.resp


.. _hmi_http__item.state_history:

item.state_history
------------------

.. list-table::
   :header-rows: 0

   * - Description
     - *Gets state history for item(s)*
   * - Parameters
     - required
   * - Returns
     - State history payload

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **k**
     - String
     - valid API key/token
     - **yes**
   * - **i**
     - Vec<String>/String
     - Item OID(s)
     - **yes**
   * - **t_start**
     - f64
     - Beginning timestamp (default: last 24 hours)
     - no
   * - **t_end**
     - f64
     - Ending timestamp (default: now)
     - no
   * - **fill**
     - String
     - Fill (nS/T/H/D/W e.g. 10T for 10-minute) + optional [:precision]
     - no
   * - **limit**
     - u32
     - Limit records to
     - no
   * - **xopts**
     - Map<String, String>
     - Extra options, depending on database type
     - no
   * - **database**
     - String
     - DB svc to get history from, w/o "eva.db." pfx (def: specified in default_db)
     - no
   * - **output_format**
     - String
     - "list" or "dict"
     - no

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/item.state_history.req
    :response: http_api_examples/item.state_history.resp


.. _hmi_http__item.state_log:

item.state_log
--------------

.. list-table::
   :header-rows: 0

   * - Description
     - *Gets state log for item(s)*
   * - Parameters
     - required
   * - Returns
     - State log payload

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **k**
     - String
     - valid API key/token
     - **yes**
   * - **i**
     - Vec<String>/String
     - Item OID(s)
     - **yes**
   * - **t_start**
     - f64
     - Beginning timestamp (default: last 24 hours)
     - no
   * - **t_end**
     - f64
     - Ending timestamp (default: now)
     - no
   * - **limit**
     - u32
     - Limit records to
     - no
   * - **xopts**
     - Map<String, String>
     - Extra options, depending on database type
     - no
   * - **database**
     - String
     - DB svc to get history from, w/o "eva.db." pfx (def: specified in default_db)
     - no

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/item.state_log.req
    :response: http_api_examples/item.state_log.resp


.. _hmi_http__log.get:

log.get
-------

.. list-table::
   :header-rows: 0

   * - Description
     - *Gets memory logger log records, requires log allow in ACL*
   * - Parameters
     - required
   * - Returns
     - List of log records

.. list-table:: Parameters
   :align: left

   * - Name
     - Type
     - Description
     - Required
   * - **k**
     - String
     - valid API key/token
     - **yes**
   * - **level**
     - String/u8
     - Log level (trace, debug, info, warn, error)
     - no
   * - **time**
     - u32
     - Recent entries, N seconds before now
     - no
   * - **limit**
     - u32
     - Limit records to
     - no
   * - **module**
     - String
     - Filter by module
     - no
   * - **rx**
     - String
     - Filter by regex in message
     - no

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/log.get.req
    :response: http_api_examples/log.get.resp


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


.. _hmi_http__set_password:

set_password
------------

.. list-table::
   :header-rows: 0

   * - Description
     - *Changes the current password (user must be logged in and session token used)*
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
   * - **k**
     - String
     - valid API key/token
     - **yes**
   * - **current_password**
     - String
     - Current user's password
     - **yes**
   * - **password**
     - String
     - New user's password
     - **yes**

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/set_password.req
    :response: http_api_examples/set_password.resp


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
     - valid API key/token
     - **yes**

..  http:example:: curl wget httpie python-requests
    :request: http_api_examples/test.req
    :response: http_api_examples/test.resp


