# The function calculates the minimum time required to visit all points in the given list 'points', where movement can be horizontal, vertical, or diagonal.
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            result += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2
        
        return result