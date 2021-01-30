P,Q,R = map(int, input().split())

M = max(P,Q,R)

if M == P:
    print(Q+R)
elif M == Q:
    print(P+R)
else:
    print(P+Q)

