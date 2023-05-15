# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = ""
        for i in range(0,len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return common
            common += strs[0][i]
            
        return common