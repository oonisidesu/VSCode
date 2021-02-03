N = int(input())
S = input()
count = 0

for i in range(N-2):
    if 'ABC' == S[i:i+3]:
        count += 1

print(count)


print(S.count('ABC'))