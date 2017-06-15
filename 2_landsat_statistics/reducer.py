#!/usr/bin/env python
import sys
key = None
val = 0.0
for line in sys.stdin:
    k, v = line.split(',')
    if (key is not None) and (key != k):
        print('key:%s, value:%d' % (k, int(float(v))))
        val = 0.0
    key = k
    val += float(v)
if key is not None:
    print('key:%s, value:%d' % (k, int(v)))
