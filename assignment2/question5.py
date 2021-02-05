inp=input("enter a number:")
check = inp.isalpha()
if check == False:
    f_no =float(inp)
    s_no = int(f_no)
    c=0; s=0
    diff =(f_no - s_no)
    if diff ==0:
        while f_no>0:
            r=f_no % 10
            s= s*10 + r
            f_no =f_no // 10
            c+=1
    if c == 2:
        print(f_no ,"entered number {inp} is a 2 digit number")
    else:
        print(f_no ,"entered number {inp} is not a 2 digit number")
else:
    print("entred input is not a number")