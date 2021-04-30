class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1:
            i_max = 0
        else:
            i_max = int(math.log(bound,x))
            
        if y == 1:
            j_max = 0
        else:
            j_max = int(math.log(bound,y))
        
        res = []
        
        for i in range(i_max+1):
            for j in range(j_max+1):
                tmp = x**i + y**j
                if tmp <= bound and tmp not in res:
                    res.append(tmp)
        return res
