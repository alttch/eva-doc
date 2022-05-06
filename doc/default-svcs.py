#!/usr/bin/env python3

import yaml
import jsonschema

SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'nam': {},
            'exe': {},
            'dsc': {},
            'ins': {}
        },
        'required': ['nam', 'exe', 'dsc'],
        'additionalProperties': False
    }
}

with open('default-svcs.yml') as fh:
    svcs = yaml.safe_load(fh)

jsonschema.validate(svcs, SCHEMA)

svcs = sorted(svcs, key=lambda k: k['nam'])

print('.. list-table::')
print()
print('   * - Suggested name')
print('     - Executable')
print('     - Description')
print('     - Install')
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
    print(f'   * - {nam}')
    print(f'     - {exe}')
    print(f'     - {dsc}')
    print(f'     - {ins}')
