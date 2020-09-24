# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
import math 

p = 0.88
q= 1-p
prob = 0

for i in [8,9,10]:
    c = math.factorial(10)/(math.factorial(i)*math.factorial(10-i))
    prob += c*(p**i)*(q**(10-i))
print(round(prob,3))

prob = 0
for i in [8,7,6,5,4,3,2,1,0]:
    c = math.factorial(10)/(math.factorial(i)*math.factorial(10-i))
    prob += c*(p**i)*(q**(10-i))
print(round(prob,3))
