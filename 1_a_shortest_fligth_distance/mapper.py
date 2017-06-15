#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.split(',')
    if len(line) != 12:
        continue
    airline_id, distance = line[1].strip(), line[10].strip()
    print('%s\t%s' % (airline_id, distance))
