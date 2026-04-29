class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ = nums[0]
        for i in nums:
            min_ = min(min_, i)
        return min_