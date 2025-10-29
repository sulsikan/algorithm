class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = 1
        cnt = 0
        while n >= binary:
            binary *= 2
            cnt += 1      
        return binary -1