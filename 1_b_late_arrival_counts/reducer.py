#!/usr/bin/env python
import sys
old_airline = None
total_delay = 0.0
total_flights = 0.0
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if len(line) != 2:
        continue
    airline_id, delay = line
    try:
        delay = float(delay)
    except ValueError:
        continue
    if (old_airline is not None) and (airline_id != old_airline):
        print('ID:%s, total flights:%d, delayed flights:%d, percentage delayed flights:%f' % (old_airline, total_flights, total_delay, (total_delay/total_flights) * 100))
        old_airline = None
        total_delay = 0.0
        total_flights = 0.0
    old_airline = airline_id
    total_flights += 1.0
    if 0.0 < delay:
        total_delay += 1.0
if old_airline is not None:
    print('ID:%s, total flights:%d, delayed flights:%d, percentage delayed flights:%f' % (old_airline, total_flights, total_delay, (total_delay/total_flights) * 100))    
