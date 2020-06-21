class Solution(object):
    def runningSum(self, nums):
        #         rst = []
        #         # nums = [1,2,3,4]
        #         for num in nums:
        #             if rst: # rst 값이 하나라도 있을때
        #                 rst.append(num + rst[len(rst) - 1]) # 추가
        #             else: # rst에 값이 아무것도 없을때
        #                 rst.append(num) # 추가

        #         return rst
        rst = []
        previousNum = 0
        for num in nums:
            previousNum += num
            rst.append(previousNum)
        return rst
