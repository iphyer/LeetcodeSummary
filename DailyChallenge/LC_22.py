class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generateParenthesisDFS(path = [], num_opening = 0, num_closing = 0):
            if num_opening > n or num_closing > num_opening: return
            
            if path and len(path) == 2*n: 
                res.append( "".join(path) )
                return
            
            generateParenthesisDFS(path + ["("], num_opening+1, num_closing)
            generateParenthesisDFS(path + [")"], num_opening, num_closing+1)
        
        generateParenthesisDFS()

        return res
    
    
""" Another Python Solution

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack([], 0, 0)
        return ans

"""
