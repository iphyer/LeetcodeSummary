class Solution:
    def originalDigits(self, s: str) -> str:
        res = []
        freq_s = Counter(s)
        # update freq table
        def update_freq(s, num):
            for ch in s:
                if freq_s[ch] > num:
                    freq_s[ch] -= num
                else:
                    del freq_s[ch]
        # single char to represent
        # z for 0,zero
        if 'z' in freq_s:
            res += (['0'] * freq_s['z'])
            update_freq("zero", freq_s['z'])
        # u for 4,four
        if 'u' in freq_s: 
            res += (['4'] * freq_s['u'])
            update_freq("four", freq_s['u'])
        # x for 6,six
        if 'x' in freq_s: 
            res += (['6'] * freq_s['x'])
            update_freq("six", freq_s['x'])
        # g for 8,eight
        if 'g' in freq_s: 
            res += (['8'] * freq_s['g'])
            update_freq("eight", freq_s['g'])
        # If one char is excluded then another number is known
        # 'f' only in 4,four(excluded by 'u') and 5,five
        if 'f' in freq_s: 
            res += (['5'] * freq_s['f'])
            update_freq("five", freq_s['f'])
        # 's' for 7,seven and 6,six(excluded by 'x')
        if 's' in freq_s:
            res += (['7'] * freq_s['s'])
            update_freq("seven", freq_s['s'])
        # 'i' for 9,nine and 8,eight(excluded by 'g')
        if 'i' in freq_s:
            res += (['9'] * freq_s['i'])
            update_freq("nine", freq_s['i'])
        # 'h' for 3,three and 8,eight(excluded by 'g')
        if 'h' in freq_s:
            res += (['3'] * freq_s['h'])
            update_freq("three", freq_s['h'])
        # 'n' for 1,one after pervious excluding 7, 9
        if 'n' in freq_s:
            res += (['1'] * freq_s['n'])
            update_freq("one", freq_s['n'])
        # only 2, two left
        if 't' in freq_s:
            res += (['2'] * freq_s['t'])
            update_freq("two", freq_s['t'])
        assert len(freq_s) == 0
        res = sorted(res)
        return "".join(res)
