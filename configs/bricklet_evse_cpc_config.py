# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# EVSE CPC Bricklet communication config

from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Thomas Hein <github@poohnet.de>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 9001,
    'name': 'EVSE CPC',
    'display_name': 'EVSE CPC',
    'manufacturer': 'poohnet',
    'description': {
        'en': 'Two SSRs',
        'de': 'Zwei SSRs'
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
'name': 'Set Value',
'elements': [('Channel0', 'bool', 1, 'in', {'default': False}),
             ('Channel1', 'bool', 1, 'in', {'default': False})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the state of the relays, *true* means on and *false* means off.
For example: (true, false) turns relay 0 on and relay 1 off.
""",
'de':
"""
Setzt den Zustand der Relais, *true* bedeutet ein und *false* aus.
Beispiel: (true, false) schaltet Relais 0 ein und Relais 1 aus.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Value',
'elements': [('Channel0', 'bool', 1, 'out', {'default': False}),
             ('Channel1', 'bool', 1, 'out', {'default': False})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the state of the relays, *true* means on and *false* means off.
""",
'de':
"""
Gibt den Zustand der Relais zurück, *true* bedeutet ein und *false* aus.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Channel LED Config',
'elements': [('Channel', 'uint8', 1, 'in', {'range': (0, 1)}),
             ('Config', 'uint8', 1, 'in', {'constant_group': 'Channel LED Config', 'default': 3})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Each channel has a corresponding LED. You can turn the LED off, on or show a
heartbeat. You can also set the LED to "Channel Status". In this mode the
LED is on if the channel is high and off otherwise.
""",
'de':
"""
Jeder Kanal hat eine dazugehörige LED. Die LEDs können individuell an- oder
ausgeschaltet werden. Zusätzlich kann ein Heartbeat oder der Kanalstatus
angezeigt werden. Falls Kanalstatus gewählt wird ist die LED an wenn
ein High-Signal am Kanal anliegt und sonst aus.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Channel LED Config',
'elements': [('Channel', 'uint8', 1, 'in', {'range': (0, 1)}),
             ('Config', 'uint8', 1, 'out', {'constant_group': 'Channel LED Config', 'default': 3})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the channel LED configuration as set by :func:`Set Channel LED Config`
""",
'de':
"""
Gibt die Kanal-LED-Konfiguration zurück, wie von :func:`Set Channel LED Config` gesetzt.
"""
}]
})
