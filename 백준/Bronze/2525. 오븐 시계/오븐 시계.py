hour,minute=map(int,input().split())
time=int(input())

if minute+time>=60:
    hour=hour+(minute+time)//60
    minute=(minute+time)%60
    if hour>=24:
        print(f"{hour-24} {minute}")
    else:
        print(f"{hour} {minute}")
else:
    print(f"{hour} {minute+time}")