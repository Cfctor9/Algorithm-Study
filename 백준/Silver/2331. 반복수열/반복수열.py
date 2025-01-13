def cal(a, p):
    result = 0
    while a > 0:
        digit = a % 10
        result += digit ** p  # 한번에 p제곱 계산
        a //= 10
    return result

def find_cycle(a, p):
    sequence = []
    while a not in sequence:
        sequence.append(a)
        a = cal(a, p)
    return sequence.index(a)  # 반복이 시작되는 위치 반환

a, p = map(int, input().split())
print(find_cycle(a, p))