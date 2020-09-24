# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem


import math 

p = 2/3.0
q = 1/3.0

prob = 0
for i in [0,1,2,3,4]:
    prob += p**i * q

print(round(prob,3))
