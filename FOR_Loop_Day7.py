n=int(input())
for i in range(1, n+1):
    star = ("* ")*i
    space = (" ")*2*(n-i)
    print(star + space*2 + star)

for i in range(1, n):
    star = ("* ")*i
    space = (" ")*(n-i)
    print(star + space*2 + star)