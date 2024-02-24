# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Phase Switcher Bricklet communication config

com = {
    'author': 'Thomas Hein <github@poohnet.de>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 9002,
    'name': 'Phase Switcher',
    'display_name': 'Phase Switcher',
    'manufacturer': 'poohnet',
    'description': {
        'en': 'Phase Switcher',
        'de': 'Phase Switcher'
    },
    'released': False,
    'documented': False,
    'discontinued': False,
    'features': [
        'device',
        'comcu_bricklet',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append({
'name': 'Channel LED Config',
'type': 'uint8',
'constants': [('Off', 0),
              ('On', 1),
              ('Show Heartbeat', 2),
              ('Show Channel Status', 3)]
})

com['packets'].append({
'type': 'function',
'name': 'Set Control Pilot Disconnect',
'elements': [('Control Pilot Disconnect', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Phases Wanted',
'elements': [('Phases Wanted', 'uint8', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get All Data',
'elements': [('Is Control Pilot Disconnected', 'bool', 1, 'out'),
             ('Phases Wanted', 'uint8', 1, 'out'),
             ('Phases Active', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})
