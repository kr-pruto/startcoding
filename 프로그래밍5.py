"""line="====="
print(line*20)
msg="congrations"
print(msg*10)
print(len(msg))
print(msg.upper()) #upper() <-문자열을 대문자로 변환
print(msg.find("gr")) #find() <-괄호 안의 문자 찾기
------------------------------
price=1000
print("%d"%price)
print("%s"%price)
num=1234567890
print("%d"%num)
print("%20d"%num)
print("%-20d %d"%(num,35))
fnum=35.1234567890
print("%f"%fnum)
print("%20f"%fnum)
print("%-20f"%fnum)
print("%20.4f"%fnum)
------------------------------
word="Python"
print(word[0])
print(word[-1])
word[0]="c"
------------------------------
O=input("첫 번째 단어를 입력해주세요")
S=input("두 번째 단어를 입력해주세요")
T=input("세 번째 단어를 입력해주세요")
print(O[0]+S[0]+T[0])
------------------------------
shopping_list=['milk','eggs','cheese','butter','cream']
print(shopping_list[2])
shopping_list[2]='apple'
print(shopping_list)
------------------------------
x=10
y=x
print(id(x))
print(id(y))
print(id(10))
x=30
print(id(x))
------------------------------
import math

a=0.1+0.1+0.1
b=0.3
print(a==b)
print(a-b)

epsilon=1e-9 #오차범위
if math.isclose(a,b): #isclose: 괄호 안의 변수의 값이 비슷하다면
    print("a와 b는 같다")
    print("잘했음")
else:
    print("a와 b는 다르다")
    print("잘했음")
------------------------------
numbers=[1,2,3,4,5]

if 3 in numbers:
    print("3이 리스트에 있습니다")
else:65
    print("3이 리스트에 없습니다")
------------------------------
list=["kim","hong","lee"]

id=input("아이디를 입력하세요 ")
if id in list:
    ps=int(input("패스워드를 입력하세요 "))
    if ps==12345678:
        print("환영합니다")
    else:
        print("패스워드가 틀렸습니다")
else:
    print("아이디가 일치하지 않습니다")
------------------------------
age=18
height=170
if age>=10 and height>=165:
    print("놀이기구를 탈 수 있다")
else:
    print("놀이기구를 탈 수 없다")
------------------------------
W=float(input("짐의 무게는 얼마입니까? "))
if W>20:
    print("무거운 짐은 20000원을 내셔야 합니다")
else:
    print("짐에 대한 수수료는 없습니다")
print("감사합니다")    
------------------------------
fir=int(input("첫 번째 정수를 입력하세요"))
sec=int(input("두 번째 정수를 입력하세요"))
if fir>sec:
    print(f"큰 수는 {fir}")
else:
    print(f"큰 수는 {sec}") 
------------------------------
pur=int(input("구입 금액을 입력하시오 "))
sal=0
if pur>=100000:
    sal=pur*0.05
    total=pur-sal
print(f"할인 금액은 {sal}입니다")
print(f"지불 금액은 {total}입니다")
------------------------------
S=input("문자열을 입력하세요")
E=len(S)%2
s=len(S)//2
if E==1:
    print("중앙 글자는",S[s])
else:
    print("중앙 글자는",S[s-1]+S[s])
------------------------------
age=15
if 20>age>=10:
    print("놀이기구를 탈 수 있습니다")
------------------------------
n=int(input("정수를 입력하세요 "))
if n==0:
    print(f"입력된 정수는 {n}입니다")
else:
    if n>0:
        print("입력된 정수는 양수입니다")
    else:
        print("입력된 정수는 음수입니다")
------------------------------
n=int(input("나이를 입력하시오 "))
if 40>n>=30:
    print("30대")
else:
    if 30>n>=20:
        print("20대")
    else:
        if 20>n>=10:
            print("10대")
------------------------------"""