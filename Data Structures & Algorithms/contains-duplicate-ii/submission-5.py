class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if map.get(nums[i], -1) != -1 and abs(map[nums[i]] - i) <= k:
                return True
            map[nums[i]] = i
        return False