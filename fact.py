def fact(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        if n in memo:
            return memo[n]
        return fact(n-1)+fact(n-2)
    
memo = {}
for i in range(10):
    val = fact(i)
    if i not in memo:
        memo[i]=val
    print(val)