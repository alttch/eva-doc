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
print('   * - Sugg.name')
print('     - Executable')
print('     - Description')
print('     - Install')
for svc in svcs:
    exe = svc['exe']
    exe_link = exe.replace('venv/bin/', 'svc/')
    exe = f':doc:`{exe}</{exe_link}>`'
    ins = svc.get('ins', '')
    if ins.startswith('py:'):
        mod = ins[3:]
        ins = (f'Requires `{mod} <https://pypi.org/project/{mod}/>`_ '
               'Python module')
    print(f'   * - {svc["nam"]}')
    print(f'     - {exe}')
    print(f'     - {svc["dsc"]}')
    print(f'     - {ins}')
