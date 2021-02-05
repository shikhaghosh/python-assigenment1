num=int(input("enter two digit number:"))
reverse=0
while num >0:
    reminder=num%10
    reverse=(reverse*10)+reminder
    num=num//10
print("%d"%reverse)