class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for ch in s:
            
            if ch == ']':
                tmp_str = ""
                while stack:
                    curr = stack.pop(-1)
                    if curr != "[":
                        tmp_str += curr
                    else:
                        break
                tmp_int = ""
                while stack:
                    curr = stack.pop(-1)
                    if curr.isnumeric():
                        tmp_int += curr
                    else:
                        stack.append(curr)
                        break
                tmp_res = tmp_str[::-1] * int(tmp_int[::-1])
                stack += [c for c in tmp_res]
            else:
                stack.append(ch)
        return "".join(stack)
    
"""
bcbc, e, f

tmp1: febcbc
tmp2: cbcbef

b,c,b,c,e,f

tmp1: fecbcb
tmp2: bcbcef

"""
