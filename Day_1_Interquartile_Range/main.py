# https://www.hackerrank.com/challenges/s10-interquartile-range/problem
import sys
import math
from collections import Counter
import operator
from statistics import median

f = open("input.txt","r")
#f = sys.stdin

total_num = int(f.readline()) # Read the first line
raw_num = f.readline() # Raed the second line which contains the numbers
raw_freq = f.readline() # Raed the second line which contains the numbers

num = [int(x) for x in raw_num.split()]
freq = [int(x) for x in raw_freq.split()]

num_full = [num[i] for i in range(len(num)) for j in range(freq[i])]


num = sorted(num_full)


def get_median_even_num(num):
    return (num[int(math.floor(len(num)-1)/2)]+num[int(math.floor(len(num))/2)])/2.0

first_q = None
third_q = None
med = None

if len(num)%2:
    half_len = math.floor(len(num)/2)
    first_half = num[:half_len]
    second_half = num[half_len+1:]
    med = num[half_len]
    first_q = get_median_even_num(first_half)
    third_q = get_median_even_num(second_half)

else:
    half_len = math.floor(len(num)/2)
    first_half = num[:half_len]
    second_half = num[half_len:]
    med= get_median_even_num(num)
    first_q=get_median_even_num(first_half)
    third_q=get_median_even_num(second_half)
    
    
print(round(third_q-first_q,1))

    