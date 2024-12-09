class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxi = mini = result = nums[0]

        for i in range(1, len(nums)):
            if nums[i]<0:
                maxi, mini = mini, maxi

            maxi = max(maxi*nums[i], nums[i])
            mini = min(mini*nums[i], nums[i])

            result = max(result, maxi)
        return result        