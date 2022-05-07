#!/usr/bin/env python3

import yaml
import jsonschema
import subprocess

SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'nam': {},
            'exe': {},
            'dsc': {},
            'ins': {},
            'txt': {},
            'tpl': {},
            'api': {}
        },
        'required': ['nam', 'exe', 'dsc'],
        'additionalProperties': False
    }
}

with open('default_svcs.yml') as fh:
    svcs = yaml.safe_load(fh)

jsonschema.validate(svcs, SCHEMA)

svcs = sorted(svcs, key=lambda k: k['nam'])

with open('default_svcs.rst', 'w') as fh:
    print('.. list-table::', file=fh)
    print(file=fh)
    print('   * - Suggested name', file=fh)
    print('     - Executable', file=fh)
    print('     - Description', file=fh)
    print('     - Install', file=fh)
    for svc in svcs:
        nam = svc['nam']
        exe = svc['exe']
        exe_link = exe.replace('venv/bin/', 'svc/')
        dsc = svc['dsc']
        nam = f':doc:`{nam}</{exe_link}>`'
        dsc = f':doc:`{dsc}</{exe_link}>`'
        ins = svc.get('ins', '')
        if ins.startswith('py:'):
            mod = ins[3:]
            ins = (f'Requires `{mod} <https://pypi.org/project/{mod}/>`_ '
                   'Python module')
        print(f'   * - {nam}', file=fh)
        print(f'     - {exe}', file=fh)
        print(f'     - {dsc}', file=fh)
        print(f'     - {ins}', file=fh)
        with open(f'./{exe_link}.rst', 'w') as sfh:
            print(svc['dsc'], file=sfh)
            print('*' * len(svc['dsc']), file=sfh)
            print(file=sfh)
            txt = svc.get('txt')
            if txt:
                print(txt, file=sfh)
                print(file=sfh)
            tpl = svc.get('tpl')
            if tpl is not None:
                print('Setup', file=sfh)
                print('=====', file=sfh)
                print(f"""
Use the template *EVA_DIR/share/svc-tpl/{tpl}*:

.. literalinclude:: ../svc-tpl/{tpl}
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create {svc["nam"]} /opt/eva4/share/svc-tpl/{tpl}

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    echo TPL.yml | ./bin/yml2mp | \\
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -
""",
                      file=sfh)
            api = svc.get('api')
            if api:
                p = subprocess.Popen([
                    '/opt/eva-util/v4/eapigen/target/x86_64-unknown-linux-musl/release/eapigen',
                    f'/opt/eva4/{api}'
                ],
                                     stdout=subprocess.PIPE)
                stdout, _ = p.communicate()
                if p.returncode != 0:
                    raise RuntimeError
                print(file=sfh)
                print(stdout.decode(), file=sfh, end='')
