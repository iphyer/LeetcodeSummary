class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #res = set()
        res = 0
        pos_char = defaultdict(list)
        for ind,ch in enumerate(s): pos_char[ch].append(ind)
        #print(pos_char)
        # for each ch in pos_char
        #  (1) 3*ch
        #  (2) ch, X, ch
        ch_keys = list(pos_char.keys())
        
        for ch_key in ch_keys:
            # check length
            if len(pos_char[ch_key]) == 1: continue
            else:
                # ch, X, ch
                # select pair from ch_key
                pos1 = pos_char[ch_key][0]
                pos2 = pos_char[ch_key][-1]
                for tmp_key in ch_keys:
                    if tmp_key != ch_key:
                        for ind in pos_char[tmp_key]:
                            if pos1 < ind < pos2:
                                res += 1
                                break
                    else:
                        if len(pos_char[ch_key]) >= 3: res += 1
        return res
                            
        """
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    # find s[j]/s[i] in later
                    if s[j] in pos_char and pos_char[s[j]][-1] > j and (s[i], s[j], s[j]) not in res:
                        res.add( (s[i], s[j], s[j]) )
                else:
                    # find s[i] in later
                    if s[i] in pos_char and pos_char[s[i]][-1] > j and (s[i], s[j], s[i]) not in res:
                        res.add( (s[i], s[j], s[i]) )
        """
        #print(res)
        #return len(res)
