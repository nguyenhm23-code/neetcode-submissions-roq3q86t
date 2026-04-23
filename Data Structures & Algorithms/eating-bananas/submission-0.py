class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hour(k: int) -> int:
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / k)
            return hour
        left, right = 1, max(piles)
        res = right 
        
        while left <= right:
            mid = (left + right ) // 2
            if get_hour(mid) <= h :
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res