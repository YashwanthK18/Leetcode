class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mi = max(nums)
        for i in nums:
            m = abs(0 - i)
            if m <= mi:
                mi = m
        if mi in nums:
            return mi
        else:
            return -1 * mi
