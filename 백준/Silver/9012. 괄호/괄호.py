class Stack:
    def __init__(self): 
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty() == 1:
            return -1
        else:
            temp = self.stack[-1]
            del self.stack[-1]
            return temp

    def peek(self):  
        return -1 if self.is_empty() == 1 else self.stack[-1]
        
    def is_empty(self):
        return 1 if len(self.stack) == 0 else 0


n = int(input())
for _ in range(n):
    quiz = input()
    stack = Stack()       # ✅ 스택 인스턴스를 각 테스트마다 새로 생성
    is_true = True        # ✅ is_true 초기화

    for p in quiz:
        if p == "(":
            stack.push("(")
        else:
            temp = stack.pop()
            if temp == "(":
                continue
            else:
                is_true = False
                print("NO")
                break

    if is_true and stack.is_empty():
        print("YES")
    elif is_true:  # 스택이 비어 있지 않으면 괄호가 안 닫힌 경우
        print("NO")
