class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # j > i and prices[j] <= prices[i]
        rst = []
        lenthOfPrices = len(prices)
        for i, price in enumerate(prices):    
            i+=1
            while i < lenthOfPrices:
                if price >= prices[i]:
                    price -= prices[i]
                    break
                i+=1
                
            rst.append(price)
        
        return rst



        