class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count1 = 0
        count2 = 0
        n = len(s)
        for i in range(n):
            if i < n // 2:
                if s[i] in vowels:
                    count1 += 1
            else:
                if s[i] in vowels:
                    count2 += 1
        return count1 == count2
