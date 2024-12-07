class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        original = x
        reversedX = 0

        while x > 0:
            reversedX = reversedX*10 + x%10
            x //= 10
         
        return original==reversedX