class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if (len(nums) <3):
            return ans
        
        nums.sort()

        for i in range(len(nums)-2):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            
            left = i+1
            right = len(nums)-1

            while (left<right):
                currSum = nums[i]+nums[left]+nums[right]
                if (currSum==0):
                    ans.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while (left<right and nums[left]==nums[left-1]):
                        left += 1
                    while (left<right and nums[right]==nums[right+1]):
                        right -= 1
                elif (currSum < 0):
                    left += 1
                elif (currSum > 0):
                    right -= 1
        return ans