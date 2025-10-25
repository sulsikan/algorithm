class Solution:
    def totalMoney(self, n: int) -> int:
        # n을 7로 나눠 몇주 넣을 건지 계산
        week = n // 7
        s = 1
        sum = 0
        while week > 0:
            for i in range(s, s+7):
                sum += i
            s += 1
            week -= 1

        # n % 7 마지막주 계산
        day = n % 7
        for i in range(s, s+day):
            sum += i

        return sum
