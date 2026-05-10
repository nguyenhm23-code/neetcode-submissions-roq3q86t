class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            mapping[num] = 1 + mapping.get(num, 0)
        sorted_items = sorted(mapping.items(), key = lambda x: x[1], reverse = True)
        res = []
        for i in range(k) :
            res.append(sorted_items[i][0])
        return res


        