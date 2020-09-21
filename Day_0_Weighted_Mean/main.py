import sys
import math
from collections import Counter
import operator

f = open("input.txt","r")
#f = sys.stdin


total_num = int(f.readline()) # Read the first line
raw_num = f.readline() # Raed teh second line which contains the numbers
raw_weight = f.readline() # Raed teh second line which contains the weight

num = [int(x) for x in raw_num.split()]
weight = [int(x) for x in raw_weight.split()]

numerator=0
for i in range(total_num):
    numerator += num[i] * weight[i]
    
print(round(numerator*1.0/(sum(weight)),1))