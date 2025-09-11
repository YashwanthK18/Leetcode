class Solution:
    def calPoints(self, operations: List[str]) -> int:
        c=0
        x=[]
        for i in operations:
            if i=='C':
                x.pop()
            elif i=='+':
                x.append(x[len(x)-2]+x[len(x)-1])
            elif i=='D':
                x.append(x[len(x)-1]*2)
            else:
                x.append(int(i))
        for i in x:
            c+=i
        return c
