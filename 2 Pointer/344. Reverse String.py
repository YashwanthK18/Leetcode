class Solution:
    def reverseString(self, nums: List[str]) -> None:
        for i in range(len(nums) // 2):
            nums[i], nums[-1 * i - 1] = nums[-1 * i - 1], nums[i]
