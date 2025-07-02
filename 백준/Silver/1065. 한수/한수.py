#백준 1065번 한수

def is_hansu(number: int) -> bool:
    # 숫자를 문자열로 바꿔서 각 자릿수를 나눠줌
    num_str = str(number)
    
    # 1자리, 2자리 수는 무조건 한수!
    if len(num_str) <= 2:
        return True
    
    # 자릿수 차이를 구해서 등차인지 확인
    gap = int(num_str[1]) - int(num_str[0])  # 첫째 자리 차이
    for i in range(1, len(num_str) - 1):
        # 앞뒤 자릿수 차이가 같지 않으면 한수가 아님
        if int(num_str[i + 1]) - int(num_str[i]) != gap:
            return False
    
    return True  # 끝까지 차이가 같으면 한수임

# 사용자로부터 숫자 입력 받기
N = int(input())

# 한수 개수 세기
count = 0
for i in range(1, N + 1):
    if is_hansu(i):
        count += 1

# 결과 출력
print(count)
