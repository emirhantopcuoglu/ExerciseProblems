# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int):
        num = str(x)
        j = -1
        for i in range(0,len(num)):
            if num[i] == num[j]:
                j -= 1
                if i == len(num) - 1:
                    return True
                else:
                    continue
            else:
                return False