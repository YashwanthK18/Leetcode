class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for i in d:
            d[i] = text.count(i)
            if i == "l" or i == "o":
                d[i] //= 2
        return min(d.values())
