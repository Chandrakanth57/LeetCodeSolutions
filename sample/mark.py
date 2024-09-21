n = 10
m = 7
bn = bin(n)[2:]
bm = bin(m)[2:].zfill(len(bn))


count = 0
for i in range(len(bm)):
    if bm[i]!=bn[i]:
        count+=1

print(count)