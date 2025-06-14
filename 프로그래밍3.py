"""x=10
y=30
t=x
x=y
y=t
print(x,y)"""


a=1
n=int(input("정수를 입력하시오 "))
for x in range(1,n+1):
    a*=x
print(f"{n}!은 {a}이다")
