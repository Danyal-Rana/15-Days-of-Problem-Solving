class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words_list = s.split()
        if words_list:
            return len(words_list[-1])
        return 0