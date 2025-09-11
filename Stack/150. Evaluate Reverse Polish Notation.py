class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                n2=int(stack.pop())
                n1=int(stack.pop())
                if i=='+':
                    stack.append(n1+n2)
                if i=='-':
                    stack.append(n1-n2)
                if i=='*':
                    stack.append(n1*n2)
                if i=='/':
                    stack.append(int(n1/n2))
        return stack[0]