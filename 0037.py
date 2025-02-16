n=int(input())
s=1
for i in range(n):
  a,b=map(int,input().split())
  if a>0 and b>0:
    s*=(abs(a-b)+1)
  elif a>0 and b<0:
    s*=(a+(abs(b)))
  elif a<0 and b>0:
    s*=(b+(abs(a)))
  elif a<0 and b<0:
    s*=abs(abs(a)-abs(b))+1
  elif a==0 or b==0:
    s*=(max(abs(a),abs(b)))
print(s%(1000000007))