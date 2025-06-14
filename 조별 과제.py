def CtoF():
    c=float(input("섭씨온도 "))
    fTemp=9.0/5.0*c+32
    return fTemp

def FtoC():
    f=float(input("화씨온도 "))
    cTemp=(f-32.0)*5.0/9.0
    return cTemp

while True:
    print("'c':섭씨온도에서 화씨온도로 변환")
    print("'f':화씨온도에서 섭씨온도로 변환")
    print("'q':종료")

    menu=input("메뉴에서 선택하세요 ")
    if menu=='c':
        fTemp=CtoF()
        print(fTemp)
    elif menu=='f':
        cTemp=FtoC()
        print(cTemp)
    elif menu=='q':
        break