class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        small_wl = dict()
        for w in wordlist:
            if w.lower() not in small_wl:
                small_wl[w.lower()] = w
        vowel_wl = dict()
        vowels = ('a', 'e', 'i', 'o', 'u')
        for w in wordlist:
            tmp = [ c if c not in vowels else '#' for c in w.lower()]
            str_tmp = "".join(tmp)
            if str_tmp not in vowel_wl:
                vowel_wl[str_tmp] = w
        res = []
        for q in queries:
            if q in wordlist:
                res.append(q)
                continue
            if q.lower() in small_wl:
                res.append(small_wl[q.lower()])
                continue
            tmp = [ c if c not in vowels else '#' for c in q.lower()]
            str_tmp = "".join(tmp)
            if str_tmp in vowel_wl:
                res.append(vowel_wl[str_tmp])
                continue
            res.append("")
        return res
