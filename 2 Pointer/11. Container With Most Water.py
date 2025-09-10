class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                if area < (r - l) * height[l]:
                    area = (r - l) * height[l]
                l += 1
            else:
                if area < (r - l) * height[r]:
                    area = (r - l) * height[r]
                r -= 1
        return area
