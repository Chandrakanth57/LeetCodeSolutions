l = [2,2,1,1,1,2,2]

d = {}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1


max_val = -1
ke = -1
for k in d.keys():
    if d[k]>max_val:
        ke = k
        max_val = d[k]
print(ke)