class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(numbers)):
            if target - numbers[i] in check:
                return [check[target - numbers[i]], i+1]
            check[numbers[i]] = i+1