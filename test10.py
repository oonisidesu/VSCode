N = int(input())
count = 0

for i in range(10):
    for j in range(10):
        if N == (i*j):
            count += 1

if count != 0:
    print("Yes")
else:
    print("No")