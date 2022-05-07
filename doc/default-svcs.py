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
            'des': {},
            'ins': {},
            'txt': {},
            'tpl': {},
            'api': {}
        },
        'required': ['nam', 'exe', 'des'],
        'additionalProperties': False
    }
}

with open('default_svcs.yml') as fh:
    svcs = yaml.safe_load(fh)

jsonschema.validate(svcs, SCHEMA)

svcs = sorted(svcs, key=lambda k: k['des'])

with open('core_svcs_toc.rst', 'w') as tfh:
    print('.. toctree::', file=tfh)
    print('    :caption: The core and services', file=tfh)
    print('    :maxdepth: 1', file=tfh)
    print(file=tfh)
    print('    core', file=tfh)
    print('    services', file=tfh)
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
            des = svc['des']
            nam = f':doc:`{nam}</{exe_link}>`'
            des = f':doc:`{des}</{exe_link}>`'
            ins = svc.get('ins', '')
            if ins.startswith('py:'):
                mod = ins[3:]
                ins = (f'Requires `{mod} <https://pypi.org/project/{mod}/>`_ '
                       'Python module')
            print(f'   * - {nam}', file=fh)
            print(f'     - {exe}', file=fh)
            print(f'     - {des}', file=fh)
            print(f'     - {ins}', file=fh)
            print(f'    {exe_link}', file=tfh)
            with open(f'./{exe_link}.rst', 'w') as sfh:
                print(svc['des'], file=sfh)
                print('*' * len(svc['des']), file=sfh)
                print(file=sfh)
                print('.. contents::', file=sfh)
                print(file=sfh)
                txt = svc.get('txt')
                if txt:
                    print(txt, file=sfh)
                    print(file=sfh)
                tpl = svc.get('tpl')
                if tpl is not None:
                    print('Setup', file=sfh)
                    print('=====', file=sfh)
                    snam = svc['nam']
                    gnam = snam
                    if snam.endswith('N'):
                        snam = snam[:-1] + '1'
                        gnam = gnam[:-1]
                print(f"""
Use the template *EVA_DIR/share/svc-tpl/{tpl}*:

.. literalinclude:: ../svc-tpl/{tpl}
   :language: yaml

Create the service using :ref:`eva-shell`:

.. code:: shell

    eva svc create {snam} /opt/eva4/share/svc-tpl/{tpl}

or using ELBUS CLI client:

.. code:: shell

    cd /opt/eva4
    cat DEPLOY.yml | ./bin/yml2mp | \\
        ./sbin/elbus ./var/elbus.ipc rpc call eva.core svc.deploy -

(see :ref:`eva.core::svc.deploy<eva.core__svc.deploy>` for more info)
""",
                      file=sfh)
                api = svc.get('api')
                if api:
                    p = subprocess.Popen(
                        ['/opt/eva4/sbin/eapigen', gnam, f'/opt/eva4/{api}'],
                        stdout=subprocess.PIPE)
                    stdout, _ = p.communicate()
                    if p.returncode != 0:
                        raise RuntimeError(svc['nam'])
                    print(file=sfh)
                    print(stdout.decode().rstrip(), file=sfh)
