# 세로 길이는 3보다 커야함
# 3 부터 순차적으로 나누어 떨어지는 수 찾고, prev에 같은 수가 있으면 중단
# prev = [3,4,6]
# 순서대로 (가-2)*세 = 옐로 를 해보고 조건에 맞으면 반환
import math
def solution(brown, yellow):
    n = int(brown + yellow)
    prev = []
    for i in range(3, int(math.sqrt(n))*2):
        if n % i == 0:
            prev.append(i)
    for col in prev:
        row = n // col
        if (row-2)*(col-2) == yellow:
            answer = [row, col]
            return answer
    