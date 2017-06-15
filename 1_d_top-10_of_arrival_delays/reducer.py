#!/usr/bin/env python
import sys
old_airline = None
delay_list = []
tmp_list = []
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if len(line) != 2:
        continue
    airline_id, tmp_list = line
    try:
        tmp_list = [int(float(x)) for x in tmp_list.split(',')]
    except ValueError:
        continue
    if (old_airline is not None) and (airline_id != old_airline):
        list_as_string = ''
        for x in delay_list:
            list_as_string += ', ' + str(x)
        print('ID:%s, top_10_delays:[%s]' % (old_airline, list_as_string.replace(',', '', 1)))
        old_airline = None
        delay_list = []
    old_airline = airline_id
    delay_list = delay_list + tmp_list
    delay_list.sort()
    if len(delay_list) > 10:
        delay_list = delay_list[(len(delay_list) - 10):]
if old_airline is not None:
    list_as_string = ''
    for x in delay_list:
        list_as_string += ', ' + str(x)
    print('ID:%s, top_10_delays:[%s]' % (old_airline, list_as_string.replace(',', '', 1)))
