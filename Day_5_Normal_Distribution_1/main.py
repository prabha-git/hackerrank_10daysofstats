# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

import math

def normal_cdf(x):
    "cdf for standard normal"
    q = math.erf(x / math.sqrt(2.0))
    return (1.0 + q) / 2.0


print(round(normal_cdf(-.5/2),3))

l1 = normal_cdf(1)
l2 = normal_cdf(0)

print(round(l1- l2,3))

