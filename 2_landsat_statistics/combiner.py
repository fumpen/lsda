#!/usr/bin/env python
import sys
import numpy as np
import pickle
from collections import Counter
model = pickle.load(open("model.save", "rb"))
count = 0
tmp_matrix = []

for line in sys.stdin:
    try:
        line = [float(l) for l in line.split(',')]
    except:
        pass
    tmp_matrix.append(line)
    count += 1
    if count >= 500:
        tmp_matrix = np.array(tmp_matrix)
        res = model.predict(tmp_matrix)
        res = Counter(res)
        for k, v in res.most_common():
            print(str(k) + ',' + str(v))
        tmp_matrix = []
        count = 0
tmp_matrix = np.array(tmp_matrix)
res = model.predict(tmp_matrix)
res = Counter(res)
for k, v in res.most_common():
    print(str(k) + ',' + str(v))
