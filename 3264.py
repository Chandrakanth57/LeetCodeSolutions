
s = "iiii"
k = ''
count = 0
f = 1
for i in s:
    k+=str(ord(i)-96)

for _ in range(f):
    count=0
    print(k)
    for i in k:
        # print(i)
        count+=int(i)
    k = str(count)
    


print(count)
