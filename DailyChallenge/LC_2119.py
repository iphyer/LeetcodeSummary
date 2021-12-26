"""

simulation

"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = reversed([i for i in str(num)])
        reversed1 = int("".join(reversed1))
        reversed2 = reversed([i for i in str(reversed1)])
        
        return int("".join(reversed2)) == num
      
      
"""

Check if there are leading zeros

== > actually the ending shall not be 0

== > not multiply of 10

"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return num % 10 != 0
