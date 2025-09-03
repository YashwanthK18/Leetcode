class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        prod=reduce(mul,nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                ans.append(int(prod/nums[i]))
            else:
                ans.append(int(reduce(mul,nums[:i]+nums[i+1:])))
        return ans