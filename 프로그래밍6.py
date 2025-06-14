"""N=int(input("성적을 입력하세요 "))
if N>=90:
    print("A")
elif N>=80:
    print("B")
elif N>=70:
    print("C")
elif N>=60:
    print("D")
else:
    print("F")
------------------------------
M=int(input("월을 입력하세요 "))
if M==2:
    print("월의 날 수는 28입니다")
elif M<=7:
    if M%2==0:
        print("월의 날 수는 30입니다")
    else:
        print("월의 날 수는 31입니다")
else:
    if M%2==0:
        print("월의 날 수는 31입니다")
    else:
        print("월의 날 수는 30입니다")
------------------------------
M=int(input("월을 입력하세요 "))
if M==2:
    print("월의 날 수는 28입니다")
elif M==4 or M==6 or M==9 or M==10:
    print("월의 날 수는 30입니다")
else:
    print("월의 날 수는 31입니다")
------------------------------
Y=int(input("년도를 입력하세요"))
if (Y%4==0 or Y%4==0) and (Y%100!=0):
    print("윤년입니다")
else:
    print("윤년이 아닙니다")
------------------------------
for x in range(10):
    print("환영")
------------------------------
for x in ["철수","영희","길동","유신"]:
    print("환영 "+x)
------------------------------
for x in range(10):
    print(x,end=" ")
------------------------------
a=0
for x in range(1,10):
    a+=x
print(a)
------------------------------
for c in "abcdef":
    print(c,end="")
------------------------------
count=int(input("카운트 숫자 입력 "))
for x in range(count,0,-1):
    print(x,end=" ")
print("발사")
------------------------------
c=0
while c<5:
    print("환영합니다")
    c+=1
print("반복 종료")
------------------------------"""
