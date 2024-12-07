class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        i = 0
        right = len(nums)-1

        while i<= right:

            if nums[i]==0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i]==1:
                i += 1
            elif nums[i]==2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1