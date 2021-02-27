N = int(input())
count = 0
l = []
h = True
for i in range(2,N):
    if h:
        for j in range(2,N):
            if i**j <= N:
                if i**j not in l: 
                    l.append(i**j) 
                    count += 1
            elif (i**j > N) and j == 2:
                h = False
                break
            else:
                break

    else:
        break
        

print(N-count)