# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import sys
import math
from collections import Counter
import operator

f = open("input.txt","r")
#f = sys.stdin

total_num = int(f.readline()) # Read the first line
raw_num = f.readline() # Raed teh second line which contains the numbers

num = [int(x) for x in raw_num.split()]

# Calculating the mean
mean_num = sum(num)/len(num)

print(round(mean_num,1))

#calculatine median
sorted_num = sorted(num)
len_num = len(sorted_num)
middle_idx_ceil,middle_idx_floor = math.ceil((len_num+1)/2.0)-1,math.floor((len_num+1)/2.0)-1

print(round((sorted_num[middle_idx_ceil]+sorted_num[middle_idx_floor])/2.0,1))

#calculating the median
num_freq = dict(Counter(sorted_num))
    
print(min([k for k, v in num_freq.items() if v == max(num_freq.values())]))




