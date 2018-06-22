print("hello Ravish")
num = int(input("Enter a number:: "))
temp = bin(num)
bi = temp[2:]
print(bi)
tempspace=[0]
sp=0
flag =True
for i in range(0,len(bi)):
    if (bi[i] == '1' and flag == True) :
        flag = False
    else:
        flag=True
        sp+=1




