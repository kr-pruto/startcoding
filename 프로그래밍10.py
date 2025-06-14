"""print(sum([1,2,3]))
#----------------------------
[i**2 for i in range(10)]
#----------------------------
list1=['All','good','things']
items=[s[0] for s in list1]
print(items)
#----------------------------
list=[90,80,20,60,70,100]
minimum=list[0]
for x in range(1,len(list)):
    if minimum>list[x]:
        minimum=list[x]
print(minimum)
#----------------------------
words=['mouse','tiger','cat','lion']
min=words[0]
for x in range(1,len(words)):
    if len(min)>len(words[x]):
        min=words[x]
print(min)
#----------------------------
numbers=[10,20,30,40,50,60,70,80,90]
result=[]
for x in numbers:
    if x>50:
        result.append(x)
print(result)
#----------------------------
def linearSearch(aList,key):
    for i in range(len(aList)):
        if key == aList[i]:
            return key, i

numbers=[10,20,30,40,50,60,70,80,90]
print(linearSearch(numbers, 50))
#----------------------------
nums=[0,10,20,30,40,50]
key=50
def linSch(nums):
    for x in range(len(nums)):
        if key==nums[x]:
            return x
        else:
            return -1
pos=linSch(nums,key)
if pos!=-1:
    print('found-position:',pos)
else:
    print('not found')
#----------------------------
data=[]
F=open(r"C:\tmp\data.txt","r",encoding="UTF8")
for line in F.readlines():
    data.append(line.strip())
print(data)
F.close()
#----------------------------
x=[[0,0]]+[[0,0]]
print(x)
x=[]
x=x+[[0,0]]
x=[]
x=x+[[0]*10]
#----------------------------
rows=3
cols=5
s=[]
for x in range(rows):
    s=s+[[0]*cols]
print(s)
#----------------------------
rows=3
cols=5
s=[[0]*cols for r in range(rows)]
print(s)
#----------------------------
a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
row=len(a)
col=len(a[0])
for x in range(row):
    for y in range(col):
        print(a[x][y],end=",")
    print()
#----------------------------
s=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
sum=0
cols=len(s[1])
for x in range(cols):
    sum+=s[1][x]
print(sum)
#----------------------------
list=[]
row=6
col=6
for x in range(row):
    list+=[[0]*col]
for i in range(row):
    for j in range(col):
        list[i][j]=i+1+j+1
print(list)
#----------------------------
def sum_mat(a,b):
    c=[]
    row=len(a)
    col=len(a[0])
    for i in range(row):
        c=c+[[0]*col]
    for i in range(row):
        for j in range(col): 
            c[i][j]=a[i][j]+b[i][j]
    return c

a=[[1,2],[2,3]]
b=[[3,4],[4,5]]
print(sum_mat(a,b))
#----------------------------
import math
def cal_circ(r):
    a=math.pi*r**2
    c=2*math.pi*r
    return (a,c)
r=float(input("원의 반지름을 입력하세요 "))
(area,circum)=cal_circ(r)
print("원의 면적=", area)
print("원의 둘레=", circum)
#----------------------------
def search_binary(list,value):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if list[mid]>value: high=mid-1
        elif list[mid]<value: low=mid+1
        else: return mid
    return -1
myList=[0,10,20,30,40,50,60,70,80,90,100]
print(search_binary(myList,50))
#----------------------------
partyA=['park','kim','lee']
partyB=['park','choi']
a=set(partyA)
b=set(partyB)
c=a.intersection(b)
d=a.union(b)
print(c)
print(d)
#----------------------------
def cnt_word(sen):
    word_list=sen.split()
    word_set=set(word_list)
    length=len(word_set)
    return length

s=input("문자열을 입력하세요")
res=cnt_word(s)
print(res)
#----------------------------"""
