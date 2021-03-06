import itertools
N = int(input())
A = list(map(int, input().split()))
l = list(itertools.combinations(A, 2))
ans = 0

for i in range(l):
    ans += (l[i][0] - l[i][1])**2

print(ans)