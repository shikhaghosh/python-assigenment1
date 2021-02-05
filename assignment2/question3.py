n1=float(input("enter the first value: "))
n2=float(input("enter the second value: "))
n3=input("enter the arithmetic oprtator: ")
if (n3== "+"):
    print("result" , n1+n2)
elif (n3== "-"):
    print("result", n1-n2)
elif (n3== "/"):
    print("result", n1/n2)
elif (n3== "*"):
    print("result", n1*n2)
else:
    print("end")