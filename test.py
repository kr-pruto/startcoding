num, num2, num3=input("세 개의 정수를 입력하세요").split()
num=int(num)
num2=int(num2)
num3=int(num3)
if(num>num2):
    if(num>num3):
        print(num)
    else:
        print(num3)
elif(num2>num3):
    print(num2)
else:
    print(num3)