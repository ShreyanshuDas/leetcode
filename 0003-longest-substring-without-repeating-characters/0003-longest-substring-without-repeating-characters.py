class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        start = 0
        max_length = 0
        for i, c in enumerate(s):
            if c in char_map and char_map[c] >= start:
                start = char_map[c] + 1
            char_map[c] = i
            max_length = max(max_length, i - start + 1)
        return max_length
