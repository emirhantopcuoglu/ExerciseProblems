# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal1 = int(a,2)
        decimal2 = int(b,2)

        result = decimal1 + decimal2

        result = bin(result)[2:]

        return result