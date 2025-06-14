"""def modify(k):
    k+=1
    print(k)
k=10
modify(k)
print(k)
#----------------------------
def modify1(msg):
    msg+=' To You'
    print(msg)
msg='Happy Brithday'
modify1(msg)
print(msg)
#----------------------------
def modify2(li):
    li+=[100,200]
list=[1,2,3,4,5]
print(list)
modify2(list)
print(list)
#----------------------------
s='전국 사과'
def daegu():
    global s
    print(s)

    s='대구 사과'
    print(s)

daegu()
print(s)
#----------------------------
def daegu(s):
    print(s)
def kwangju(s):
    print(s)
def main():
    s='대구 사과 최고'
    daegu(s)
    kwangju(s)
main()
#----------------------------
x=20
y=30
y,x=x,y
print(x)
print(y)
#----------------------------
def sub(x,y):
    global a
    a=7
    x,y=y,x
    b=3
    print(a,b,x,y)
a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y)
#----------------------------
PI=3.141592
def cir_Area(r):
    c_A=r**2*PI
    return c_A
def cir_Round(r):
    c_R=2*r*PI
    return c_R
def main():
    r=float(input('원의 반지름을 입력하세요 '))
    print(f'원의 면적:{cir_Area(r)}')
    print(f'원의 둘레:{cir_Round(r)}')
main()
#----------------------------
sum=lambda x,y:x+y
print('정수의 합:',sum(10,20))
print('정수의 합:',sum(20,10))
#----------------------------
def fact(n):
    if n==0:
        return 1
    if n>=1:
        return n*fact(n-1)    #순환(회계)함수
num=int(input('정수 '))
print(fact(num))
#----------------------------
from fibo import *
fib(30)
fib2(30)
#----------------------------
scores=[]
for _ in range(10):
    sc=int(input('성적='))
    scores.append(sc)
print(scores)
#----------------------------
scores=[32,56,64,72,12]
scores[0]=80
scores[1]=scores[0]
print(scores)
#----------------------------
scores=[32,56,64,72,12]
for i in range(len(scores)):
    print(i,scores[i])
for i in range(len(scores)):
    scores[i]=i*10
print(scores)
#----------------------------
sc=[]
sc=list()
sc2=['h','e','r']
sc2=list('her')
sc3=[0,1,2,3,4]
sc3=list(range(5))
#----------------------------
def cal_sum(ex_list):
    sum=0
    for i in ex_list:
        sum+=i
    return sum
def main():
    ex_list=[1,2,3,4,5]
    sum=cal_sum(ex_list)
    print(f'리스트 {ex_list}의 합: {sum}')
#----------------------------
STD=5
list=[]
sum=0
for i in range(STD):
    score=int(input('성적을 입력하세요 '))
    list.append(score)
    sum+=score
avg=sum/len(list)
exStd=0
for i in range(len(list)):
    if list[i]>=80:
        exStd+=1
print(f'성적의 평균은 {avg}입니다')
print(f'80점 이상 성적을 받은 학생은 {exStd}명 입니다')
#----------------------------
dogs_name=[]
while True:
    name=input('강아지의 이름을 입력하시오(종료시에는 엔터키)')
    if name=='':
        break
    dogs_name.append(name)
print(dogs_name)
#----------------------------"""