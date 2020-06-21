class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        numberOfMax = max(candies)
        return [candy + extraCandies >= numberOfMax for candy in candies]
