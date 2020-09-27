import math
import sys

f = open("input.txt","r")
#f = sys.stdin

x = []
y = []
for line in f.readlines():
    x.append(int(line.split()[0]))
    y.append(int(line.split()[1]))


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

def pearson(x,y):
    return covariance(x,y)/(std(x)*std(y))

b = pearson(x,y) * (std(y)/std(x))

a = sum(y)/(len(y)*1.0) - b * (sum(x)/(len(x)*1.0))
print(round(a + b * 80,3))




