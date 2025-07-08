# 입력 받기
n, m = map(int, input().split())

# 첫 번째 행렬 A 입력
A = [list(map(int, input().split())) for _ in range(n)]

# 두 번째 행렬 B 입력
B = [list(map(int, input().split())) for _ in range(n)]

# 결과 행렬을 생성하고 출력
for i in range(n):
    result = [A[i][j] + B[i][j] for j in range(m)]
    print(*result)
