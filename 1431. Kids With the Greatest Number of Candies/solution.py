class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = candies[0]
        result = []
        for i in range(len(candies)):
                if max < candies[i]:
                    max = candies[i]     
        for j in range(len(candies)):
            result.append((candies[j]+extraCandies)>=max)
        return result     