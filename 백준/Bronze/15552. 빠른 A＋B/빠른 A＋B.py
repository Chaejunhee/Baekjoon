import sys
# n=int(input("n"))
n=int(sys.stdin.readline())

for _ in range(n): 
    A, B =map(int, sys.stdin.readline().split())
    print(A+B)