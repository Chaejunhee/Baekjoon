total=int(input())
var=int(input())
result=0
for _ in range(var):
    N,P=map(int,input().split())
    result+=N*P
print("Yes" if (result==total)==True else "No")