class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotated = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[0] < nums[i]:
                break
            rotated += 1
        if rotated == 0:
            return nums[0]
        return nums[len(nums) - rotated]
            