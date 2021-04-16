class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        Reference Video is here to check:
        possible arrows and reasonable results
        
        https://www.youtube.com/watch?v=_mbnPPHJmTQ
        
        """
        # edge cases
        if not preorder: return False
        # general cases
        num_arrows = 1
        preorder = preorder.split(",")      
        n = len(preorder)
        
        for i in range(n):
            if num_arrows == 0:
                # arrows used up but strs not
                return False
            
            if preorder[i] == '#':
                num_arrows -= 1
                if num_arrows < 0:
                    # currently there must be great than zero arrows
                    return False
            else:
                num_arrows += 1
        return num_arrows == 0
