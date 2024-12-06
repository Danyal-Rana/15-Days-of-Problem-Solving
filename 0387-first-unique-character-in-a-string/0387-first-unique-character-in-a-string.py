class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = {}

        for char in s:
            charCount[char] = charCount.get(char, 0) + 1

        for i, char in enumerate(s):
            if (charCount[char]==1):
                return i
        
        return -1