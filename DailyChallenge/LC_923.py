class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq = Counter(arr)
        res = 0
        ans_pair = set()
        keys = list(freq.keys())
        
        for i in range(len(keys)):
            for j in range(len(keys)):
                remain = target - keys[i] - keys[j]
                if remain in keys:
                    # check if counted 
                    tmp = sorted([remain, keys[i], keys[j]])
                    if tuple(tmp) not in ans_pair:
                        # check equality conditions
                        # 3 same numbers
                        if tmp[0] == tmp[1] == tmp[2]:
                            if freq[tmp[0]] >= 3:
                                res = res + int((freq[tmp[0]])* (freq[tmp[0]]-1)* (freq[tmp[0]]-2) / 6 )
                                ans_pair.add(tuple(tmp))
                            else:
                                pass
                        # 2 same numbers
                        elif tmp[0] == tmp[1]:
                            if freq[tmp[0]] >= 2:
                                res = res + int((freq[tmp[0]]) * (freq[tmp[0]]-1) / 2) * freq[tmp[2]]
                                ans_pair.add(tuple(tmp))
                            else:
                                pass
                        elif tmp[1] == tmp[2]:
                            if freq[tmp[1]] >= 2:
                                res = res + int((freq[tmp[1]]) * (freq[tmp[1]]-1)/ 2) * freq[tmp[0]]
                                ans_pair.add(tuple(tmp))
                            else:
                                pass
                        elif tmp[0] == tmp[2]:
                            if freq[tmp[2]] >= 2:
                                res = res + int((freq[tmp[2]] * (freq[tmp[2]]-1)) / 2)* freq[tmp[1]]
                                ans_pair.add(tuple(tmp))
                            else:
                                pass
                        else: # no same number
                            res = res + freq[tmp[0]] * freq[tmp[1]] * freq[tmp[2]]
                            ans_pair.add(tuple(tmp))
        return res%(10**9 + 7)
