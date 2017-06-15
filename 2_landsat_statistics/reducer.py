#!/usr/bin/env python
import sys
count = 0
tmp_class = None
for line in sys.stdin:
    try:
        line = line.strip()
        line = line.split(',')
        c_class, c_count = line
        if (tmp_class is not none) and (c_class != tmp_class):
            print('class:%s, number of predictions:%d' % (tmp_class, count))
            count = 0
        tmp_class = c
        count += int(c_count)
    except:
        pass
if tmp_class is not none:
    print('class:%s, number of predictions:%d' % (tmp_class, count))
