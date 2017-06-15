#!/usr/bin/env python
import sys
import numpy as np
import pickle
model = pickle.load(open("model.save", "rb"))
for line in sys.stdin:
    try:
        vec = np.fromstring(a, sep=',').reshape(1, 9)
        pred = model.predict(vec)[0]
        print('%d' % pred)
    except:
        pass
        
    
