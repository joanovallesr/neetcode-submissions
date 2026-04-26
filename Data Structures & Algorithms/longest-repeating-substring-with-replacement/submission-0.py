class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            curr_len = r - l + 1
            if curr_len - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(max_freq, r - l + 1)

        return res