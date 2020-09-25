# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

import math

def normal_cdf(x):
    "cdf for standard normal"
    q = math.erf(x / math.sqrt(2.0))
    return (1.0 + q) / 2.0


print(round((1-normal_cdf(1))*100,2))

print(round((1-normal_cdf(-1))*100,2))

print(round(normal_cdf(-1)*100,2))

