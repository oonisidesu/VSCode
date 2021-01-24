i = list(map(int, input().split()))
# 標準入力この書き方もある
# ↓
# A, B, T = map(int, input().split())
A = i[0]
B = i[1]
T = i[2]
TT = T + 0.5

print(int((TT // A) * B))

# formatの書き方
# print("{0} {1}".format((P_1 - N),(P_2 - N)))