class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1, freq2 = Counter(nums1), Counter(nums2)
        res = []
        for k in freq1.keys():
            if k in freq2.keys():
                min_freq = min(freq1[k], freq2[k])
                res += [k for _ in range(min_freq)]
        return res
