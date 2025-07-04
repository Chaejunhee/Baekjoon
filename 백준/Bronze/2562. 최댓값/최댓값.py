m=0
index=0
for i in range(9):
    n=int(input())
    if n>m:
        m=n
        index=i
print(m)
print(index+1)