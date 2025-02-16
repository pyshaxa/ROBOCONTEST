n=int(input())
k=0
for i in range(1,n+1):
  for l in range(i):
    k+=1
    print(k,end=' ')
  print()