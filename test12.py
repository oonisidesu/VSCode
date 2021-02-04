S = input()

mylist = ["A", "C", "G", "T"]
count = 0
d = 0

for i in range(len(S)):
    if (S[i] in mylist):
        count += 1
    else:
        count = 0
    
    d = max(d, count)

print(d)