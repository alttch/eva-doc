Migration to V4
***************

.. contents::

Why migrate to EVA ICS v4
=========================

* **Total refactoring**. Most of EVA ICS code has been rewritten in `Rust
  <https://www.rust-lang.org>`_ - a modern language, which provides near-C
  speeds with no safety costs. According to tests of typical customers' tasks,
  version 4 is about **50x faster** than v3.

* **New micro-kernel model**. With :doc:`the new model </architecture>`, all
  item logic was moved to external services, which allows version 4 to process
  dozens of millions items on a single node, about **1000x more** than in v3.

* **Node scalability**. V4 node has extremely great multiprocessing support and
  memory management and can utilize as much system resources as there are
  available. Furthermore, for heavy-loaded systems, nodes can be split into
  multiple "points", by moving :doc:`services </services>` to neighbor
  computers.

* **New AAA**. The new :doc:`/aaa` architecture, much cleaner and much more
  powerful.

* **IaC and Deployment for everything**. V3 had great deployment features, but
  V4 is much better - everything can be deployed, undeployed and redeployed as
  on a single node, as on all selected nodes of customers' clouds.

* **Extension unification**. Version 3 had 6 types of extension. In version 4
  there is the only one type of extension - services. Which communicate with
  the core and between each other using `ELBUS <https://elbus.bma.ai/>`_ - an
  in-house IPC-bus, developed especially for high-loaded industrial
  applications.

* **Automation logic**. V3 had the only logic snippets: Python macros. In V4
  :ref:`lmacro` no longer means a Python script with lots of built-ins, but ANY
  scenario, executed by a software or hardware PLC, written in any language and
  optimized especially for customers' needs.

* **Backward compatibility**. Reborn inside, refactored outside. EVA ICS v4 is
  **99.9% compatible** with all existing HMI web applications and almost with
  all V3 Python macros.

* **Nevertheless no vendor lock-in**. EVA ICS is still open-source,
  open-licensed, can work with any equipment and requires no vendor-cloud
  connection. You build your cloud - you own your cloud. Private and secure.

Migration
=========

V3 nodes in V4 cluster
----------------------

V3 nodes can be connected as secondaries to V4 nodes, see
:doc:`/svc/eva4-svc-repl-legacy` for more details.

The service provides all replication and interaction features, however there is
not possible to do remote deployment for V3 nodes from V4 central ones.

For the deployment tasks, consider leaving a few V3 SFA nodes and connect
secondaries to both V3 and V4 centrals.

Logic
-----

EVA ICS v4 core has the minimal logic to improve its speed and scalability.

The only in-core logic is:

- **logic.range** item property, which sets the status to -1 (ERROR) if the
  value is non-numeric or out-of-range.

- lvar op functions (set/reset/clear/toggle)

- when lvar status is set to 0, the state can not be updated with RAW events,
  unless "force" field is present and set to true

.. note::

    The v4 lvar logic is different from v3: while v3 functions
    reset/clear/toggle operate with lvar value, v4 functions modify lvar
    status.

    The logic is implemented this way because v4 lvars have got "enabled"
    property, which replaces zero-status. When migrating to v4, consider
    carefully reviewing v3 macros and scripts, especially timers.

    To avoid logic confusion, it is not recommended to mix v3 and v4 lvars in a
    single cloud.

Item states
-----------

* unit nstatus/nvalue fields are removed. Instead, units now have "act" field,
  which is larger than zero if actions are pending/running.

* item expiration is handled now by external state expiration services. To let
  EVA JS framework handle lvar timers correctly, BOTH an expiration service
  must be setup plus "meta.expires" lvar field set.

HMI
___

Administration methods
~~~~~~~~~~~~~~~~~~~~~~

All system methods have been moved to :ref:`bus calls
<hmi_http__bus__TARGET_SVC__METHOD>`.

Calling methods of other services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`hmi_http__x__TARGET_SVC__METHOD`.

HMI HTTP API methods
~~~~~~~~~~~~~~~~~~~~

Methods were changed as the following:

V3 method           V4 Method
==================  =====================================
test                test (unchanged)
login               login (unchanged)
logout              logout ("k" parameter changed to "a")
state               item.state
state_history       item.state_history
state_log           item.state_log
log_get             log.get
action              action (unchanged)
action_toggle       action.toggle
result              action.result
kill                action.kill
terminate           action.terminate
run                 run (unchanged)
set                 lvar.set
reset               lvar.reset
clear               lvar.clear
toggle              lvar.toggle
increment           lvar.incr
decrement           lvar.decr
get_neighbor_list   session.list_neighbors
set_token_readonly  session.set_readonly

V3 methods, listed above, still work, but are deprecated and will be removed
soon. Please update your HMI applications to use the new method names.

Serving data from the registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* */%pvt* URI has been replaced with **/:pvt**, as "%" in URI field may cause
  problems for certain clients.

* */%pub* URI has been replaced with **/:pub** for the same reason.

Server templates
~~~~~~~~~~~~~~~~~

V4 HMI service provides :doc:`tera templates </hmi/server_templates>`, which
have functionality similar to Jinja2, however some complex structures may be
incompatible. Consider testing all server templates before migrating production
applications.

V4 HMI templates have no built-in functions at the moment, for built-in
variables, see :doc:`/hmi/server_templates`.

HMI tokens
~~~~~~~~~~

:doc:`/svc/eva-hmi` issues tokens only for user/password pair. Tokens for API
keys are not supported.

Python macros
-------------

* All macro functions now require OIDs, calling methods with short IDs is not
  allowed any longer.

* Macros do not have the global variable "\_source" any longer.

* Macro arguments / keyword arguments are no longer converted to
  integers/floats automatically (except if run with :ref:`eva-shell`)

* Macro extensions are no longer supported and should be converted either into
  Python modules or in EVA ICS services.

See also :doc:`/lmacro/py/python_macros`.
