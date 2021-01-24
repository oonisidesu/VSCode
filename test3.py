i = list(map(int, input().split()))
# 標準入力この書き方もある
# ↓
# A, B, T = map(int, input().split())
A = i[0]
B = i[1]
T = i[2]
TT = T + 0.5

print(int((TT // A) * B))