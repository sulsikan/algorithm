class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        zero_positions = [i for i, v in enumerate(nums) if v==0 ]

        def simulate(start: int, dr: int) -> bool:
            # 작업용으로 사본 만들기
            a = nums[:]
            curr = start # 시작 인덱스 지정
            d = dr

            while 0 <= curr < N:
                if a[curr] == 0:
                    curr += d
                else:
                    a[curr] -= 1
                    d *= -1
                    curr += d

            return all(x==0 for x in a)

        ans = 0
        for i in zero_positions:
            if simulate(i, 1):
                ans += 1
            if simulate(i, -1):
                ans +=1
        
        return ans