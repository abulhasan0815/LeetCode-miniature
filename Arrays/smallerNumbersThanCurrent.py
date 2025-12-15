# The function returns a list where each element at index 'i' represents the count of numbers in the input list 'nums' that are smaller than 'nums[i]'.
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}

        for i, v in enumerate(temp):
            if v not in d:
                d[v] = i

        ret = []

        for val in nums:
            ret.append(d[val])

        return ret