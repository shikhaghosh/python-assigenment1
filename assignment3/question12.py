nterms=int(input("Enter the number: "))
n1=0
n2=1
count=2
if nterms<=0:
    print("please enter a positive integer")
elif nterms==1:
    print("Fibonacci series:")
    print(n1)
else:
    print("Fibonacci series:")
    print(n1,"",n2,end=' ')
    while count<nterms:
        nth=n1+n2
        print(nth,end=' ')
        n1=n2
        n2=nth
        count +=1