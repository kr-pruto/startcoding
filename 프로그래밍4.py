"""a=1000
r=0.05
n=10

T=a*(1+r)**n
print(T)
------------------------------
sec=1000
m=60
M=sec//m
sec=sec%m
print(M,sec)
------------------------------
x=10
y=3
X=x//y
Y=x%y
print(x,"을" ,y,"로 나눈 몫 =",X)
print(x,"을" ,y,"로 나눈 나머지 =",Y)
------------------------------
x=10
print(f"결과:{x}")
print("결과:"+str(x))
print("결과:%d %o %X %i %f"%(x,x,x,x,x))
------------------------------
N=int(input("원하는 숫자를 입력하세요"))
if N%2==0:
    print("짝수입니다")
else:
    print("홀수입니다")

N=int(input("원하는 숫자를 입력하세요"))
if N%2:          #N에 3이 왔다고 했을 때 2로 나누면 1이 나오고 컴퓨터 내에선 1을 true로 간주하기 때문에 가능
    print("홀수입니다")
else:
    print("짝수입니다")
------------------------------
id=['일','월','화','수','목','금','토']
D={"일요일":0,"월요일":1,"화요일":2,"수요일":3,"목요일":4,"금요일":5,"토요일":6}
T=input("오늘의 요일(문자로):")
d=D[T]
n=(d+10)%7
print(id[n]+'요일')
------------------------------
abs(-3) #절댓값
------------------------------
from math import * #math라는 라이브러리에서 *와 관련된 도구를 모두 불러오기기
print(sqrt(2**2+3**2))  #루트
------------------------------
import math
math.sprt(2**2+3**2)
------------------------------
import math
time1=10/20
T=math.sqrt(3**2+4**2)
time2=T/10
time3=T/30
time4=8/20
total=time1+time2+time3+time4
print(total)
------------------------------
from gtts import gTTS

N=input("이름이 무엇인가요? ")
P="만나서 반갑습니다." + N + "씨!"
tts=gTTS(text=P, lang="ko")
tts.save("test.mp3")
------------------------------
name=input("이름이 무엇인가요?")
print("만나서 반갑습니다. "+name+"씨!")
age=input("나이는 몇살이야?")
print("네,그러면 당신은 벌써 "+age+"살 이군요 "+name+"씨!")
------------------------------
first=int(input("첫 번째 정수 "))
second=int(input("두 번째 정수 "))
re=first+second
print("합은"+str(re))
------------------------------
x=10
print(type(x))
print("%o,%d,%x"%(x,x,x))

x=0o12 #8진법
y=0xa  #16진법
z=0b1010 #2진법
print(x,y,z)

round(3.14159)
round(3.14159,2) #소수점 2자리까지 반올림
------------------------------
age=int(input("나이를 입력해주세요 "))
af10=age+10
print(f"10년 후면 {af10}살살이 되시는군요!")
------------------------------
msg="Merry Christmas!"
print(msg)
msg=62
print(msg)
msg="철수가 '안녕'이라 뒤돌아섰다"
text=\"""광주의 새벽이
열렸다.
그 때 한 소년이 외쳤다.
자유를 외친 대한민국.\"""
print(text)
------------------------------
msg="dosen\'t" # \ <-기능 삭제
print(msg)
msg="\"yes\" he said."
m="1번째줄\n2번째줄"
print(m)
m="1번째줄\t2번째줄"
print(m)
print("C:\some\\name")
print(r'C:\some\name') # r <- 문장 내의 모든 기능 무시"""