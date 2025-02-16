from math import *
a=int(input())
b=input().split()
d=[]
for i in b:
  c=(sqrt(8*int(i)+1)-1)/2
  if c%1==0:
    d+='1'
  else:
    d+='0'
print(*d,sep='')