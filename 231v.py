# n=9
# f=False
# for i in range(n//2):
#     v=n/2
#     n=v
#     # print(n)
#     if n==1.0:
#         f=True
#         break

# if f==True:
#     print("pwr")

# else:
#     print("not")

    
n = 1024
flag = True
while n!=1:
    if n%2!=0:
        flag = False
        break
    n=n//2

if flag:
    print("2P")
else:
    print("N2P")







