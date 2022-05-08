Legacy (v3) replication service
*******************************

.. contents::

Installing/updating
===================

Legacy (v3) replication service is not included into EVA ICS distribution. To install/update it,
either edit "eva/config/python-venv" :doc:`registry</registry>` key, specify
the desired version in "extra" section (e.g. *eva4-repl-legacy>=0.0.1*) and rebuild the
Python virtual environment (*/opt/eva4/sbin/venvmgr build*). Or execute:

.. code:: shell

    /opt/eva4/sbin/venvmgr add eva4-repl-legacy
    # or 
    /opt/eva4/sbin/venvmgr add eva4-repl-legacy==N # where N = version number

The latest eva-shell version number can be obtained from
https://pypi.org/project/eva4-repl-legacy/

