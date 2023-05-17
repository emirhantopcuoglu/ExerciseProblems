# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        if index == -1:
            return -1
        else:
            return index