# given value n check wether its a valid perfect square

# example if 16 given return true 
# if given 7 return false because 4*4 16 num no num*num = 7 

n = 16

for i in range(1,n):
    if i*i == n:
        print("perfect",i)
        break

