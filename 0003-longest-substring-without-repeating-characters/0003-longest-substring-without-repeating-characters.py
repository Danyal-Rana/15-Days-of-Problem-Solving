class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start = 0
        maxLen = 0

        for end in range(len(s)):
            while(s[end] in charSet):
                charSet.remove(s[start])
                start+=1
            charSet.add(s[end])
            maxLen = max(maxLen, end-start+1)
        return maxLen