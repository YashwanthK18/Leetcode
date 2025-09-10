class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for i in s:
            if i.isalnum():
                ss += i.lower()
        if ss != ss[::-1]:
            return False
        return True
