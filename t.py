n,k=map(int,input().split())
def f(x):
  s=list(str(x))
  s.sort()
  s="".join(s)
  g1=int(s[::-1])
  g2=int(s)
  return g1-g2
for i in range(k):n=f(n)
print(n)