print("enter three numbers:")
a1,a2,a3=int(input()),int(input()),int(input())
if(a1<a2<a3 or a3<a2<a1):
    print(a2,"is the second smallest")
elif(a2<a3<a1 or a1<a3<a2):
    print(a3,"is the second smallest") 
else:
     print(a1,"is the second smallest")     