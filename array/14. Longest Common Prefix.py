class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = ""
        strs.sort(key=len)
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[0][i] != strs[j][i]:
                    return ans
            ans += strs[0][i]
        return ans
