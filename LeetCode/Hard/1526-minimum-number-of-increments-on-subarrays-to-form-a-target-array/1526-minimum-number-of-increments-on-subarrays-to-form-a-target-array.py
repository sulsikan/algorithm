class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # 붙어있는 부분만 1씩 증가시켜 타켓 배열이 되는데 되는 최소 횟수
        # 아이디어 : 각 요소가 이전 요소에 비해 얼마나 증가했는지 세는 것
        res = prev = 0
        for x in target:
            if x > prev:
                res += x-prev
            prev = x
        return res
        