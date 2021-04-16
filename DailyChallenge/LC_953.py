class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # edge case
        if len(words) == 1: return True
        # general case
        order_dict = defaultdict(int)
        for ind,val in enumerate(order):
            order_dict[val] = ind+1
        n = len(words)

        for i in range(1,n):
            for j in range(len(words[i-1])):
                if j >= len(words[i]):
                    # words[i-1] and words[i] has the same starting str
                    # and words[i-1] is longer than words[i]
                    return False
                # Found first different character 
                if words[i-1][j] != words[i][j]:
                    if order_dict[words[i-1][j]] > order_dict[words[i][j]]:
                        return False
                    else:
                        # two words are sorted
                        # then there's no need to check remaining letters
                        break
        # all word in correct order    
        return True
