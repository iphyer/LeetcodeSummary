class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            try:
                val = int(token)
                stack.append(val)
            except ValueError:
                n1 = stack.pop()
                n2 = stack.pop()
                if token == "+":
                    stack.append(n1+n2)
                elif token == "-":
                    stack.append(n2-n1)
                elif token == "*":
                    stack.append(n1*n2)
                elif token == "/":
                    stack.append( int(n2/n1) )
                else:
                    print(token)
                    print("error!")
        return stack[-1]
