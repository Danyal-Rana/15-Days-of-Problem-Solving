class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            idx = abs(n)-1;
            nums[idx] = -abs(nums[idx])
        
        return [i + 1 for i, num in enumerate(nums) if num > 0]

        