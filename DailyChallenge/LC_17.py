class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        
        dig_ch_map = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        if len(digits) == 1: return [ch for ch in dig_ch_map[int(digits)]]
        
        res = [""]
        for dig in digits:
            res = [s+ch for s in res for ch in dig_ch_map[int(dig)]]
        return res
