#백준 2675번

T = int(input())  

for _ in range(T):
    count, word = input().split()  
    for j in word:
        print(j*int(count),end='')
    print()