class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        l = [[] for _ in range(numRows)]
        x = -1
        j = 0
        for i in s:
            if j == 0 or j == numRows - 1:
                x *= -1
            if x == 1:
                l[j].append(i)
                j += 1
            else:
                l[j].append(i)
                j -= 1
        ans = ""
        for i in l:
            ans+=''.join(i)
        return ans
