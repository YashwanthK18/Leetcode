class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        start = nums[0]
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == (nums[i - 1] + 1):
                k += 1
            else:
                if k == 0:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(nums[i - 1]))
                k = 0
                start = nums[i]
            if i == len(nums) - 1:
                if k > 0:
                    ans.append(str(start) + "->" + str(nums[i]))
                else:
                    ans.append(str(nums[i]))

        return ans
