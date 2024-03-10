class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_index = 0
        i=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] !=0:
                last_non_zero_index = i
                break
        j=0
        while  j<len(nums) and j< last_non_zero_index :
            if nums[j] == 0:
                #print(j)
                nums.append(nums.pop(j))
                last_non_zero_index-=1
                if j != 0:
                    j-=1
            else:
                j+=1
