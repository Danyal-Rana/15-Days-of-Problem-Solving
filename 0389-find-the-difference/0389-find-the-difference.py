class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCounter = Counter(s)
        tCounter = Counter(t)

        diff = tCounter-sCounter

        return list(diff.keys())[0]