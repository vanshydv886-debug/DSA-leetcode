class Solution(object):
    def jump(self, nums):
        n = len(nums)
        jump = 0
        left = 0 
        right = 0
        while right < n-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest 
            jump += 1
        
        return jump
        