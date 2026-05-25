class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 1:
            return False
        l,r = 0,1
        while l < len(nums) and r < len(nums):
            if nums[l] == nums[r] and abs(r - l) <= k:
                return True
            if abs(r - l) > k:
                l += 1
                r = l + 1
                continue
            r += 1
        return False
        