class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        lastSeen = {}
        left = 0
        for idx, c in enumerate(s):
            cLastSeen = lastSeen.get(c)
            if cLastSeen is not None and cLastSeen >= left:
                longest = max(longest, idx - left)
                left = cLastSeen + 1
            lastSeen[c] = idx
        
        longest = max(longest, len(s) - left)
        
        return longest