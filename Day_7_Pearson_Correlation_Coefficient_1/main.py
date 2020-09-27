import math
import sys

f = open("input.txt","r")
#f = sys.stdin

total_num = int(f.readline()) # Read the first line
raw_x = f.readline() # Raed the second line which contains the numbers
raw_y = f.readline() # Raed the third line which contains the numbers

x = [float(x) for x in raw_x.split()]
y = [float(y) for y in raw_y.split()]

def covariance(x,y):
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)
    numerator = 0
    for i in range(len(x)):
        numerator += ((x[i] - x_mean) * (y[i] - y_mean))
    cov = numerator/len(x)
    return cov
        
    
def std(x):
    x_mean = sum(x)/len(x)
    return math.sqrt(sum([(e-x_mean)**2 for e in x])/len(x))


print(round(covariance(x,y)/(std(x)*std(y)),3))

