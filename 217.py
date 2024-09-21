nums = [1,2,3,4]

d = {}


for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1


flag = False

for i in d.keys():
    if d[i]>1:
        flag = True

print(flag)