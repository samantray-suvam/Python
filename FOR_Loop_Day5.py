# n=int(input())
# first_num=int(input())
# smallest=first_num

# for i in range(n-1):
#     num=int(input())
#     if num<smallest:
#         smallest=num
# print(smallest)


# m=int(input())
# n=int(input())
# count=0
# num_div_by_6=""
# for num in range(m, n+1):
#     if num%6==0:
#         count+=1
#         num_div_by_6 += str(num) + (" ")
# if count==0:
#     print("No Numbers Found")
# else:
#     print(num_div_by_6)


# n=int(input())
# sum=0
# for i in range(1, n+1):
#     num=int(str(1)*i)
#     sum+=num
# print(sum)


# n=int(input())
# first_num=int(input())
# smallest=first_num

# for i in range(n-1):
#     num=int(input())
#     if num<smallest:
#         smallest=num
# print(smallest)


# m=int(input())
# n=int(input())
# num_div_by_9=""
# count=0
# for num in range(m,n+1):
#     if num%9==0:
#         count+=1
#         num_div_by_9+=str(num) + (" ")
# if count==0:
#     print("No Numbers found")
# else:
#     print(num_div_by_9)


# m=int(input())
# n=int(input())
# total_count=0

# for num in range(m, n+1):
#     dig_count=len(str(num))
#     total_count+=dig_count
# print(total_count)


# n=int(input())
# for i in range(1, n+1):
#     term=int(("2")*i)
#     print(term)


#     x=int(input())
# n=int(input())
# sum=0
# for i in range(1, n+1):
#     num=str(x) * i
#     term=int(num) ** 2
#     sum+=term
# print(sum)


# x=int(input())
# n=int(input())
# sum=0
# for i in range(1, n+1):
#     num=int(str(x) * i)
#     sum+=num
# print(sum)


# string=input()
# count=0
# for char in string:
#     is_vowel=(char=="a") or (char=="e") or (char=="i") or (char=="o") or (char=="u")
#     if is_vowel:
#         count+=1
# if count>2:
#     print("String has more than two vowels")
# else:
#     print("String doesn't have more than two vowels")


#     n=int(input())
# is_div=False
# for i in range(2, 10):
#     if n%i == 0:
#         is_div=True

# if is_div==True:
#     print("Divisible Number")
# else:
#     print("Indivisible Number")