class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        lower_bound = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high)// 2
            if nums[mid] >= target:
                lower_bound = mid
                high = mid - 1
            else :
                low = mid + 1
        return lower_bound
        