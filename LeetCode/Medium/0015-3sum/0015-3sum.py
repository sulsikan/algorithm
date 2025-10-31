class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 브루트 포스로 계산하면 O(n ** 3)이지만 
        # 투포인터로 계산하면 O(n ** 2)의 시간복잡도를 갖는다.
        result = []
        # 투포인터는 정렬되어있는 배열과 사용할 때 유용
        nums.sort()
        # 기준이 되는 i를 정하고 나머지 부분을 투포인터로 계산할 것
        for i in range(len(nums)-2):
            # 값이 같으면 안되는 조건
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left +=1
                    right -=1
        return result