lit=[]
n=int(input())
c=input()
count=0
lit=list(map(int,(c.split())))
find=int(input())
for i in lit:
    if i==find:
        count+=1

print(count)