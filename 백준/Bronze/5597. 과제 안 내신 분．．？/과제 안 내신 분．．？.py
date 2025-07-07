arr=list(range(1,31))
for _ in range(28):
    n=int(input())
    arr.remove(n)
arr.sort()
print(arr[0])
print(arr[1])