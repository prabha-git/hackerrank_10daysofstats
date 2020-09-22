# https://www.hackerrank.com/challenges/s10-quartiles/problem
import sys
import math
from collections import Counter
import operator
from statistics import median

f = open("input.txt","r")
#f = sys.stdin

total_num = int(f.readline()) # Read the first line
raw_num = f.readline() # Raed the second line which contains the numbers

num = [int(x) for x in raw_num.split()]

num = sorted(num)


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
    
print(int(first_q))
print(int(med))
print(int(third_q))