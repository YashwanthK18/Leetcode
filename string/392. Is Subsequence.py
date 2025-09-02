class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        if s == "":
            return True
        for i in t:
            if i == s[x]:
                x += 1
                if x == len(s):
                    return True
        return False
