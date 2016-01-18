#!/usr/bin/env python

import json
import os

d = []
for fn in sorted(os.listdir('.')):
    if fn.startswith('rides20k') and fn.endswith('.txt.json'):
        d.append(json.load(open(fn)))

json.dump(d, open('combined.json', 'wb'))
