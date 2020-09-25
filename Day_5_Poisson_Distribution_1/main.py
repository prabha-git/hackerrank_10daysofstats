# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

import math

l = 2.5
k = 5

p = ((l**k) * (math.e ** -l))/math.factorial(k)

print(round(p,3))