class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # digits[i] is a digit from '1' to '9'.
        # so need to consider 0
        str_n = [ch for ch in str(n)]
        len_n = len(str_n)
        len_digits = len(digits)
        ans = 0
        # length of number smaller than n
        for i in range(1, len_n):
            ans += len_digits**i
        
        # the same length with n
        # Loop through str_n and then using prefix bool to check if needs
        # to do another round of digits checking
        # https://zxi.mytechroad.com/blog/math/leetcode-902-numbers-at-most-n-given-digit-set/
        
        for i in range(len_n):
            FLAG_same_digit = False
            for d in digits:
                if d < str_n[i]:
                    ans += len_digits ** (len_n - i - 1)
                if d == str_n[i]:
                    FLAG_same_digit = True
                    break
            if not FLAG_same_digit: return ans
        # means FLAG_same_digit is true even for the last digit of n
        return ans + 1
