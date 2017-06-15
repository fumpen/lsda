#!/usr/bin/env python
import sys
count = 0
tmp_class = None
for line in sys.stdin:
    try:
        c = int(line)
        if (tmp_class is not none) and (c != tmp_class):
            print('%d, %d' % (tmp_class, count))
            count = 0
        tmp_class = c
        count += 1
    except:
        pass
if tmp_class is not none:
    print('%d, %d' % (tmp_class, count))
