s1=float(input('enter marks for subject 1 :'))
s2=float(input('enter marks for subject 2 :'))
s3=float(input('enter marks for subject 3 :'))
s4=float(input('enter marks for subject 4 :'))
total=(s1+s2+s3+s4)
avg=total/4
print('avg' , avg)
if avg>=90 and avg<=100:
    print('Grade A')
elif avg>=80 and avg<=89:
    print('Grade B')
elif avg>=70 and avg<=79:
    print('Grade C')
elif avg>=60 and avg<=69:
    print('Grade D ')        
elif(avg>=40):
    print ('Pass')
else:
    print ('Fail')