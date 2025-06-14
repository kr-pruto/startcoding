"""for x in range(10,0,-1):
    for _ in range(x):
        print(' ',end="")
    print()
#----------------------------
n=int(input("정수를 입력하세요 "))
x=1
a=1
while x<=n:
    a*=x
    x+=1
print(f"{n}!={a}")
#----------------------------
for x in range(1,10):
    print(f"3*{x}={3*x}")
#----------------------------
a=1
while a<=9:
    print(f"3*{a}={3*a}")
    a+=1
#----------------------------
sum=0
num=1
while num<=100:
    if num%3==0:
        sum+=num
    num+=1        
print(f"1부터 100까지의 모든 3의 배수의 합은 {sum}입니다")
#----------------------------
a=0
n=int(input("정수를 입력하세요 "))
while True:
    t=n%10
    a+=t
    n=n//10
    if n<10:
        a+=n
        break
print(a)
#----------------------------
import random

print("숫자 게임 환영")
comnum=random.randint(1,100)
tries=0
while tries<10:
    tries+=1
    guess=int(input("1~100 사이 숫자를 입력하세요 "))
    if comnum==guess:
        print("정답! 시도 횟수",tries)
        break
    elif comnum<guess:
        print("DOWN!")
    else:
        print("UP!")
if guess!=comnum:
    print("답",comnum)
print("프로그램을 종료합니다")
#----------------------------
sum=0
num=0
avg=0
print("종료하려면 음수를 입력하시오")
while True:
    grade=int(input("성적을 입력하시오 "))
    if grade<0:
        break
    sum+=grade
    num+=1
if num>0:
    avg=sum/num
print(avg)
#----------------------------
fruit="apple"
for i in range(len(fruit)):
    print(fruit[i],end=" ")

a=0
while a<len(fruit):
    print(fruit[a],end=" ")
    a+=1
#----------------------------
orig=input("문자열을 입력하세요 ")
str=orig.lower()
vows='aeiou'
res=''
for i in str:
    if i not in vows:
        res+=i
print(res)
#----------------------------
vowcnt=0
concnt=0
orig=input("문자열을 입력하세요 ")
str=orig.lower()
vows='aeiou'
for i in str:
    if i not in vows:
        concnt+=1
    else:
        vowcnt+=1
print(f"모음의 개수 {a}")
print(f'자음의 개수 {b}')
#----------------------------
orig=input("문자열을 입력하세요 ")
str=orig.lower()
VOWS='aeiou'
for i in range(len(str)):
    if str[i] in VOWS:
        print(i)
#----------------------------
orig=input("문자열을 입력하세요 ")
str=orig.lower()
VOWS='aeiou'
for i in range(len(str)):
    if str[i] in VOWS:
        print(i, str[i])
#----------------------------
orig=input("문자열을 입력하세요 ")
str=orig.lower()
VOWS='aeiou'
for i, c in enumerate(orig):   #enumerate <-문자와 문자의 인덱스를 각 변수에 반환해주는 함수
    if c in VOWS:
        print(i, c)
#----------------------------
statement=input("문자열을 입력하세요 ")
alphas=0
digits=0
spaces=0
for c in statement:
    if c.isalpha(): #문자열 개수 측청해주는 메소드
        alphas+=1
    if c.isdigit(): #숫자의 개수 측정해주는 메소드
        digits+=1
    if c.isspace(): #스페이스 개수 측정해주는 메소드
        spaces+=1
print(alphas)
print(digits)
print(spaces)
#----------------------------
processed=''
raw=input("게좌번호를 입력하세요 ")
for i in raw:
    if i not in "-":
        processed+=i
print(processed)
#----------------------------"""

