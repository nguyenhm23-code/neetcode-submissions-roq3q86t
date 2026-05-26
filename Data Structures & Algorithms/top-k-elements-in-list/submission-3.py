class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, 0)
        map = dict(sorted(map.items(), key = lambda item: item[1], reverse =True))
        res = list(map.keys())[:k]
        return res
        