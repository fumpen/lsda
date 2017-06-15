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
    if len(line) != 4:
        continue
    airline_id, delay, delay_squared, flight_count = line
    try:
        delay = int(float(delay))
        delay_squared = int(float(delay_squared))
        flight_count =  int(float(flight_count))
    except ValueError:
        continue
    if (old_airline is not None) and (airline_id != old_airline):
        m = float(total_delay) / float(total_flight_count)
        d = float(math.pow(total_delay, 2)) / float(total_flight_count)
        d = (float(total_delay_squared) - d) / float(total_flight_count)
        d = math.sqrt(d)
        print('ID:%s, mean:%f, deviation:%f' % (old_airline, m, d))
        old_airline = None
        total_delay, total_delay_squared, total_flight_count = 0, 0, 0
    old_airline = airline_id
    total_delay += delay
    total_delay_squared += delay_squared
    total_flight_count += flight_count
if old_airline is not None:
    """
    m = float(total_delay) / float(total_flight_count)
    d = float(math.pow(total_delay, 2)) / float(total_flight_count)
    d = (float(total_delay) - d) / float(total_flight_count)
    d = math.sqrt(d)
    print('ID:%s, mean:%f, deviation:%f' % (old_airline, m, d))
    """
    pass
