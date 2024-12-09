class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        result = []

        while left<=right:
            leftVal = nums[left]
            rightVal = nums[right]
            leftSqr = leftVal*leftVal
            rightSqr = rightVal*rightVal

            if (leftSqr>rightSqr):
                result.append(leftSqr)
                left += 1
            else:
                result.append(rightSqr)
                right -= 1
        return result [::-1]