"""def say_hello(name,msg):
    print(f"안녕, {name}야, {msg}")

say_hello("철수","잘 지냈니!")
say_hello("영희","이따 동아리에서 보자")
say_hello("지연","반가워")
#----------------------------
def get_sum(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    return sum

value=get_sum(1,10)
print(value)
value=get_sum(1,20)
print(value)
value=get_sum(1,100)
print(value)
#----------------------------
def square(n):
    return n**2
value=square(10)
print(value)
#----------------------------
def square(n):
    result=n**2
    return result
value=square(10)
print(value)
#----------------------------
def get_max(x,y):
    t=max(x,y)
    return t
value=get_max(10,20)
print(value)
value=get_max(30,32)
print(value)
#----------------------------
def get_max(x,y):
    if x>y:
        return x
    else:
        return y
value=get_max(10,20)
print(value)
value=get_max(30,32)
print(value)
#----------------------------
def FtoC(f):
    c=(f-32)*5/9
    return c
temp_f=float(input("화씨온도를 입력하세요 "))
temp_c=FtoC(temp_f)
print(temp_c)
#----------------------------
def power(x,y):
    result=1
    for _ in range(y):
        result*=x
    return result
value=power(10,5)
print(value)
#----------------------------
def main():
    print(power(10,2))

def power(x,y):
    result=1
    for _ in range(y):
        result*=x
    return result
#----------------------------
from random import *

def genPasswd(length):
    passwd=''
    word="1234567890qwertyuiopasdfghjklzxcvbnm"
    for _ in range(length):
        idx=randrange(len(word)-1)
        passwd+=word[idx]
    return passwd

val=genPasswd(6)
print(val)
val=genPasswd(6)
print(val)
val=genPasswd(6)
print(val)
#----------------------------
def greet(name,msg='잘 지냈니'):
    print("안녕",name+',',msg)
greet("철수","좋은 아침")
greet("영희")
#----------------------------
def mul(x,y):
    return x*y
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
res=mul(x=20,y=30)
f_res=add(x=10,y=res)
print(f_res)
#----------------------------
def exam_func(*args):
    for a in args:
        print(a)
exam_func(1,2,3,4,5,6,7,8)
exam_func(1,2,3,4,5)
#----------------------------"""
def exam_func(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")
exam_func(a=1,b=2,c=3,d=4,e=5)