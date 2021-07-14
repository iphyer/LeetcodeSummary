class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pos_s = defaultdict(list)
        pos_t = defaultdict(list)
        for ind,ch in enumerate(s):
            pos_s[ch].append(ind)
        for ind,ch in enumerate(t):
            pos_t[ch].append(ind)
        checked = set()
        # check position matched or not
        for ch_s, ch_t in zip(s, t):
            if ch_s not in checked:
                checked.add(ch_s)
                if pos_s[ch_s] != pos_t[ch_t]:
                    return False
        return True
        
        
 class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping_s_t = {}
        mapping_t_s = {}
        
        for c1, c2 in zip(s, t):
            
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
            
        return True
      
class Solution:
    
    def transformString(self, s: str) -> str:
        
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            
            if c not in index_mapping:
                index_mapping[c] = i
                
            new_str.append(str(index_mapping[c]))
        
        return "".join(new_str)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
