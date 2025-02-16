t=int(input())
while t>0:
  t=t-1
  x,y=map(int,input().split())
  if (x//2>y):
    a=y*2+1
  else:
    a=(x-y-1)*2
  print(a)