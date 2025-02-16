a,b=map(int,input().split())
r=2
for i in range(a):
  r=r*r%b
print(r)