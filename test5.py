A,B = map(int, input().split())

if A >= 6 and A <= 12:
    print(B//2)
elif A <= 5:
    print(0)
else:
    print(B)