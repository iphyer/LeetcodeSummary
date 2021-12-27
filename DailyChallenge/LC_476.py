class Solution:
    def findComplement(self, num: int) -> int:
        str_bin_num = [ch for ch in bin(num)[2:]]
        ans = 0

        for ch in str_bin_num:
            if ch == '0':
                ans = ans * 2 + 1
            else:
                ans = ans * 2
        return ans
    
    
"""

One bit operations

"""

class Solution:
    def findComplement(self, num):
        todo, bit = num, 1
        while todo:
            # flip current bit
            num = num ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return num
    
"""

BitMask Operations

"""

from math import log2
class Solution:
    def findComplement(self, num):
        # n is a length of num in binary representation
        n = floor(log2(num)) + 1        
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = (1 << n) - 1
        # flip all bits
        return bitmask ^ num
    
"""

BitMask Operations with Built-in Functions

"""
class Solution:
    def findComplement(self, num):
        return (1 << num.bit_length()) - 1 - num
