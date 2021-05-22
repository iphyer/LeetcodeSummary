class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []

        pos_dict = defaultdict(list)
        for ind,ch in enumerate(pattern):
            pos_dict[ch].append(ind)
        pos_arr = sorted(pos_dict.values())

        for word in words: 
            # check pos index 
            curr_pos_dict = defaultdict(list)
            for ind,ch in enumerate(word):
                curr_pos_dict[ch].append(ind)
            curr_pos_arr = sorted(curr_pos_dict.values())
            if curr_pos_arr == pos_arr:
                res.append(word)
        return res
