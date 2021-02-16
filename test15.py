A,B,K = map(int, input().split())

n = 100

while(K>0):
    if(A%n == 0) and (B%n == 0):
        K -= 1
    
    n -= 1


print(n)
