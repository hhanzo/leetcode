class Solution:
    def maxArea(self, height: List[int]) -> int:
        j =len(height)-1
        i =0
        vol = 0
        while (i!=j and i<j):
            vol1 = 0
            if height[i] < height[j]:
                vol1 = height[i]*(j-i)
            else: 
                vol1 = height[j]*(j-i)
            if vol1 > vol:
                vol = vol1
            if height[i]< height[j]:
                i+=1
            else:
                j-=1
        return vol