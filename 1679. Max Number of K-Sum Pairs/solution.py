class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        operations = 0 
        while(i<j):
            if nums[i]+nums[j] < k: 
                i+=1
            elif nums[i]+nums[j] > k:
                j-=1
            else:
                j-=1
                i+=1
                operations+=1
        return operations