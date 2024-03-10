class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float ('inf')

        for n in nums:
            if n < first:
                first = n
            elif first < n and n < second:
                second = n
            elif first < second and second < n:
                return True
        
        return False