class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        d = defaultdict(int)
        s1 = set(r)
        for i in s1:
            d[i] += r.count(i) - m.count(i)
        for i in d:
            if d[i] > 0:
                return False
        return True
