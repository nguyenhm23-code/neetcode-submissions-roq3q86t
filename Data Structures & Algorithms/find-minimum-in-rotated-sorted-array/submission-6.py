class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if r == 0:
            return nums[0]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] > nums[l]:
                r = mid - 1
            else:
                r = mid
            if l == r:
                return nums[l]
                
        return nums[mid]