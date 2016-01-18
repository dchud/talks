#!/usr/bin/env python

import json
import sys


stations = {}
for line in open('station-locations.txt'):
    loc, lat, lon = line.strip().split(',')
    stations[loc] = (lat, lon)


if __name__ == '__main__':
    data = []
    fn = sys.argv[1]
    for line in open(fn):
        count, loc = line.strip().split(' ', 1)
        try:
            lat, lon = stations[loc]
            rec = {
                'loc': loc,
                'lat': float(lat),
                'lon': float(lon),
                'count': int(count),
                'percent': float(count) / 300
                }
            data.append(rec)
        except:
            pass
    json.dump(data, open(fn + '.json', 'wb'))
