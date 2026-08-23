class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        greater = {}

        for num in nums2:

            while stack and stack[-1] < num:
                smaller = stack.pop()
                greater[smaller] = num

            stack.append(num)

        result = []

        for num in nums1:
            result.append(greater.get(num, -1))

        return result