l = [1,2,3]
s = ""
for i in l:
    s+=str(i)

print(s,type(s))
num = int(s)
num+=1
num = str(num)
fin = []
for k in num:
    fin.append(int(k))

print(fin)