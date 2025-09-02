class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = len(nums1)
        for j in range(x - m):
            nums1[m + j] = nums2[j]
        nums1 += nums2[x - m :]
        nums1.sort()
