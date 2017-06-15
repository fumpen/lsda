#!/usr/bin/env python
import sys
import math
old_airline = None
total_delay = 0
total_delay_squared = 0
total_flight_count = 0
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if len(line) != 2:
        continue
    airline_id, delay = line
    try:
        delay = int(float(delay))
    except ValueError:
        continue
    if (old_airline is not None) and (airline_id != old_airline):
        print('%s\t%d\t%d\t%d' % (old_airline, total_delay, total_delay_squared, total_flight_count))
        old_airline = None
        total_delay, total_delay_squared, total_flight_count = 0, 0, 0
    old_airline = airline_id
    total_delay += delay
    total_delay_squared += math.pow(delay, 2)
    total_flight_count += 1
if old_airline is not None:
    print('%s\t%d\t%d\t%d' % (old_airline, total_delay, total_delay_squared, total_flight_count))
