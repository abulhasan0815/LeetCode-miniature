# The function finds two indices in the input list 'nums' such that the numbers at those indices add up to the given 'target'.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, v in enumerate(nums):
            look = target - v

            if look in d:
                return i, d[look]
            
            d[v] = i