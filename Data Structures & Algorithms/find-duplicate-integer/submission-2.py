class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low < high:
            count = 0
            mid = (low + high)//2
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return high
        