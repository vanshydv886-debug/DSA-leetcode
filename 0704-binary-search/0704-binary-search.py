class Solution(object):
    def search(self, nums, target):
        def binarysearch(nums, low, high):
            if low > high:
                return -1

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarysearch(nums, mid+1, high)
            else:
                return binarysearch(nums, low, mid-1)
        return binarysearch(nums, 0, len(nums) - 1)
        
        