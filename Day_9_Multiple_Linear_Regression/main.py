from sklearn import linear_model
import sys

f = open("input.txt","r")
#f = sys.stdin

m , n= list(map(int,f.readline().split())) # Read the first line
 
x=[]
y=[]
 
#reading the training data
for i in range(n):
    data = list(map(float,f.readline().split()))
    x.append(data[:m])
    y.append(data[m])
    
lm = linear_model.LinearRegression()

lm.fit(x,y)

a = lm.intercept_
b = lm.coef_  

# reading the testing data
n = int(f.readline())
x=[]
for i in range(n):
    data = list(map(float,f.readline().split()))
    target = a
    for i in range(m):
        target+= data[i]*b[i]
    print(round(target,2))

