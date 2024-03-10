class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]* len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums)):
            result[(len(nums)-1-j)] *= suffix
            suffix *= nums[(len(nums)-1-j)]
        return result