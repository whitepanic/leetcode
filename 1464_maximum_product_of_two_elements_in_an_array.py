class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        return (sortedNums[-1] - 1) * (sortedNums[-2] - 1)
        