u=int(input("Enter your consumed unit:"))
if(u<=300):
    totalbill=u*7
    print(totalbill)
elif(800>=u>300):
    totalbill=(u-300)*9+(300*7)
    print(totalbill)
elif(1500>=u>800):
    totalbill=(u-800)*12+(u-300)*9+(300*7)
    print(totalbill)
else:
    totalbill=(u-1500)*15+(u-800)*12+(u-300)*9+(300*7)
    print(totalbill)