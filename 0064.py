k, n = map(int, input().split())
s=((k-2)*n**2-(k-4)*n)//2
print(s%(10**9+7))