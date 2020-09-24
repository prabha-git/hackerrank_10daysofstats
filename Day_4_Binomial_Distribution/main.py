# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

import math 

p = 0.52153110047
q= 1-p
prob = 0

for i in [3,4,5,6]:
    c = math.factorial(6)/(math.factorial(i)*math.factorial(6-i))
    prob += c*(p**i)*(q**(6-i))

print(prob)
