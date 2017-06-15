#!/usr/bin/env python
import sys
old_airline = None
delay_list = [] 
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
        list_as_string = ''
        for x in delay_list:
            list_as_string += ',' + str(x)
        print('%s\t%s' % (old_airline, list_as_string.replace(',', '', 1)))
        old_airline = None
        delay_list = []
    old_airline = airline_id
    if len(delay_list) < 10:
        delay_list.append(delay)
    else:
        if delay_list[0] < delay:
            delay_list[0] = delay
    delay_list.sort()
if old_airline is not None:
    list_as_string = ''
    for x in delay_list:
        list_as_string += ',' + str(x)
    print('%s\t%s' % (old_airline, list_as_string.replace(',', '', 1)))
