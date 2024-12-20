class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = 0
        n = len(s)

        for i in range(n):
            if (i<n-1 and romanToInt[s[i]]<romanToInt[s[i+1]]):
                ans -= romanToInt[s[i]]
            else:
                ans += romanToInt[s[i]]
        return ans