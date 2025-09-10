class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        m = float("inf")
        a = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if m > abs(target - total):
                    m = abs(target - total)
                    a = total
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return a
