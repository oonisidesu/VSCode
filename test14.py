#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

N = int(input())
count = 0
for i in range(1, N+1):
    d = []
    d = divisor(i)

    if ((i % 2) != 0) and (len(d) == 8):
        count += 1

print(count)
