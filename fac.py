def fact(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        
        return fact(n-1)+fact(n-2)
    

for i in range(20):
    print(fact(i))