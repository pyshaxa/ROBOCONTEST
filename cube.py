import math
a=int(input())
l=[None]*a
for i in range(0,a):
    l=int(input())
    k=pow(l, 1/3)
    d=k//1
    f=k%1
    if k-d==0:
        print('YES')
    else:
        print('NO')
