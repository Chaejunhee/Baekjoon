# A:65 Z:90 a:97 z:122
# ord("Z") 
# chr(65)
word=input()
arr=[]
for _ in range(123):
    arr.append(0)

# print(arr)
for i in range(0,len(word)):
    for alphabet in range(65,91):
        if word[i]==chr(alphabet) or word[i]==chr(alphabet+32):
            arr[alphabet] += 1
max_index=arr.index(max(arr))
arr.sort()
m=arr.pop()
check = True if m == arr[-1] else False
if check!=False:
    print("?")
else:
    print(chr(max_index))