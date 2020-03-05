from random import random
from math import sqrt
from tqdm import tqdm
darts = 1000000000
hits = 0
for x in tqdm(range(1, darts)):
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / darts)
print("PI: %s" % str(pi))
