class Solution:
    def customSortString(self, order: str, str: str) -> str:
        res = ""
        freq = Counter(str)
        
        for ch in order:
            if ch in freq:
                res += ch * freq[ch]
                freq.pop(ch)
        if freq:
            for ch in freq.keys():
                res += ch * freq[ch]
        return res
