row=int(input("enter a number:"))
for i in range(row+1,0,-1):
    for j in range(0,i-1):
        print("A",end=' ')
    print("\n")