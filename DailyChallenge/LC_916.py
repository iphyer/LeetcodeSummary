class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        freq_B = Counter(B[0])
        
        for i in range(1,len(B)):
            freq_w = Counter(B[i])
            for key in freq_w.keys():
                if key in freq_B:
                    # update for more char
                    if freq_B[key] < freq_w[key]:
                        freq_B[key] = freq_w[key]
                    else:
                        continue
                else:
                    freq_B[key] = freq_w[key]
        for w in A:
            freq_w = Counter(w)
            notFound = False
            for key in freq_B.keys():
                if key in freq_w.keys() and freq_w[key] >= freq_B[key]:
                    pass
                else:
                    notFound = True
                    break
            if not notFound: res.append(w)
        return res
                        
