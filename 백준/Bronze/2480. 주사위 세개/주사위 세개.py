A,B,C=map(int,input().split())
if (A==B) and (B==C):
    prize=10000+A*1000
elif (A==B):
    prize=1000+A*100
elif (C==B):
    prize=1000+B*100
elif (A==C):
    prize=1000+A*100
else:
    prize=100*max(A,B,C)
print(prize)