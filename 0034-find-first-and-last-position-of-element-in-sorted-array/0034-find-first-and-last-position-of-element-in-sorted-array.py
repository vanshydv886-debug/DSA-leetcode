class Solution(object):
    def searchRange(self, nums, target):
        def lower_bound(nums, target):
            n = len(nums)
            lower_bound = n
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    lower_bound = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return lower_bound

        def upper_bound(nums, target):
            n = len(nums)
            upper_bound = n
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    upper_bound = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return upper_bound

        lb = lower_bound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = upper_bound(nums, target)

        return [lb, ub - 1]