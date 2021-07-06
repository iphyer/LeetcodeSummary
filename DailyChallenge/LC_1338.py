class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr) 
        N = len(arr)
        # greedy
        val_key_list = sorted([(freq[key], key) for key in freq.keys()], reverse = True)
        res = 0
        l = N

        while val_key_list and l>(N//2):
            curr_freq, curr_key = val_key_list.pop(0)
            l -= curr_freq
            res += 1
        return res
        
  # Bucket Sort
  
  class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        frequencies = list(cnt.values())
        maxFreq = max(frequencies)
        bucket = [0] * (maxFreq + 1)
        for freq in frequencies:
            bucket[freq] += 1

        ans, removed, half = 0, 0, len(arr) // 2
        freq = maxFreq
        while removed < half:
            ans += 1
            while bucket[freq] == 0: freq -= 1
            removed += freq
            bucket[freq] -= 1
        return ans
