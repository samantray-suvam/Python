# m=int(input())
# sum=0
# for i in range(1,m+1):
#     if (m%i)==0:
#         sum+=i
# print(sum)


n=int(input())
prod=1
for i in range(1,11):
    prod=n*i
    print(str(n) + " x " + str(i) + " = " + str(prod))