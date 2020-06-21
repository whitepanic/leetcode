class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        data = dict()
        for number in arr:
            if number in data.keys():
                data[number] += 1
            else:
                data[number] = 1
        
        lstCounts = [ n for n in data.values()]
        total = len(lstCounts)
        for i, cnt in enumerate(sorted(lstCounts)):
            k -= cnt
            if k == 0:
                return total - i - 1
            elif k < 0:
                return total - i
        
