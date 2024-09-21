l1 = [1,4,5]
l2 = [2,7,6]

p = len(l1)
q = len(l2)

l3 = []
i , j, k = 0,0,0
while i<q and j<p and k<p+q:
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1

    k+=1

    print(l3)
