# The function finds the missing number in a list containing n distinct numbers taken from 0 to n.
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)