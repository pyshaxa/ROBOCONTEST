n=int(input())
r=n
w=0
x=0
q=0
z=[]
a=2
while r>1:
  if r%a==0:
    r//=a
    if r!=1:
      z.append(a)
    else:
      z.append(a)
  else:
    a+=1
for i in range(len(z)):
  w=z[i]
  while w>0:
    b=w%10
    w//=10
    q+=b
while n>0:
  p=n%10
  n//=10
  x+=p
if x==q:
  print('1')
else:
  print('0')