def bs(num):
    if num <1:
        return False
    
    start , end = 1,num
    while start<=end:
        mid = start+(end-start)//2
        if mid*mid == num:
            return True
        elif mid*mid < num:
            start = mid+1
        else:
            end = mid-1

    return False

for i in range(20):
    print(bs(i))
