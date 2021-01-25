N,K = map(int, input().split())
S = input()
l = []
a = ""

for i in range(N):
    l.append(S[i])

l[K-1] = l[K-1].lower()

for j in range(N):
    a += l[j]

print(a)

# print(S[:K-1] + S[K-1].lower() + S[K:])