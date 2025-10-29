class Solution:
    def trap(self, height: List[int]) -> int:
        # max 높이를 입력 받고
        # 2차원 배열로 만들어서
        # 숫자 1사이에 있는 0의 갯수 세기

        # 투포인터를 최대로 이동
        if not height :
            return 0
        
        left, right = 0, len(height)-1
        left_max, right_max = 0,0
        volume = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume