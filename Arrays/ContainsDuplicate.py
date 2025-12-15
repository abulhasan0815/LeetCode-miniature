# The function checks if there are any duplicate elements in the input list 'nums'.
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True