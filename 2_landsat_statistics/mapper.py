#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    if len(line.split(',')) == 9:
        print('%s' % line)
    
        
    
