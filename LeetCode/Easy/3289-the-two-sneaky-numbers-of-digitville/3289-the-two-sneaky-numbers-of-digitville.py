class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        N=len(nums)
        sneaky_nums = []
        for i in range(N-2):
            if nums.count(i) != 1:
                sneaky_nums.append(i)

        return sneaky_nums