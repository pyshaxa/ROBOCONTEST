n=int(input())
odd=[]
for i in range(n):
  k=int(input())
  l=(k*k)%1000000007
  odd.insert(i,l)
for i in range(n):
  print(odd[i])