class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        l = list(set(nums))
        l.sort()
        c = 1
        m = 1
        for i in range(len(l) - 1):
            if l[i] + 1 == l[i + 1]:
                c += 1
                if m < c:
                    m = c
            else:
                c = 1
        return m
