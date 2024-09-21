n = 27
flag = True
if n>=0:
    while n!=1:
        if n%3!=0:
            flag = False
            break
        n=n//3
else:
    flag = False


print(flag)