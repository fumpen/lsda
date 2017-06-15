#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.split(',')
    if len(line) != 12:
        continue
    airline_id, delay = line[1].strip(), line[6].strip()
    if delay == '':
        delay = '0'
    print('%s\t%s' % (airline_id, delay))
