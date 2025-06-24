x=int(input())
n=int(input())
sum=0

for i in range(1, n+1):
    power = 2 * i 
    term = x ** power
    
    if i%2==0:
        term = -term
    sum+=term
print(sum)