s = [1,2,3,4]

res = [[]]

for i in s:
    res+=[c + [i] for c in res]

print(res)