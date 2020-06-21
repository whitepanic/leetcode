class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        consisting = 2
        rst = [0] * len(nums)
        for i, num in enumerate(nums):
            if i < n:
                rst[i*consisting] = num
            else:
                rst[(i-n)*consisting+1] = num

        return rst
