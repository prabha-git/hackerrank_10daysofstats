# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

import math


# Machine A
l = 0.88
cost_a = 160 + 40 *(l+l**2)
print(round(cost_a,3))

# Machine B
l = 1.55
cost_b = 128 + 40 *(l+l**2)
print(round(cost_b,3))
