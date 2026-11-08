class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if(target-nums[i] in nums):
                l=i
                k=nums.index(target-nums[i])
        return [k,l]