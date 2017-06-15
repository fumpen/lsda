#!/usr/bin/env python
import sys
old_airline = None
old_distance = -1
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if len(line) != 2:
        continue
    airline_id, distance = line
    try:
        distance = float(distance)
    except ValueError:
        continue
    if (old_airline is not None) and (airline_id != old_airline):
        print('ID:%s, min-distance:%d' % (old_airline, old_distance))
        old_airline = None
        old_distance = -1
    old_airline = airline_id
    if (old_distance == -1) or (old_distance > distance):
        old_distance = distance
if old_airline is not None:
    print('ID:%s, min-distance:%d' % (old_airline, old_distance))
        
