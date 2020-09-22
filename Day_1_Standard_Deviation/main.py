# https://www.hackerrank.com/challenges/s10-standard-deviation/problem
import sys
import math
from collections import Counter
import operator


f = open("input.txt","r")
#f = sys.stdin

total_num = int(f.readline()) # Read the first line
raw_num = f.readline() # Raed the second line which contains the numbers

num = [int(x) for x in raw_num.split()]

mu = sum(num)/len(num)

sq_diff = 0
for i in range(len(num)):
    sq_diff += (num[i]-mu)**2
    
print(round(math.sqrt(sq_diff/len(num)),1))