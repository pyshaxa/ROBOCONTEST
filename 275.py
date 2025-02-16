a=int(input())
b=input()
s=0
arr=[]
l=0
a1=0
for i in range(a):
  d=b[i]
  if d=='U':
    s+=1
  else:
    s-=1
  if s==-1 and a1==0 :
      l+=1
  a1=s
print(l)