import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = (x**2 + y**2)
            minHeap.append([distance, x, y])
        
        res = []
        heapq.heapify(minHeap)

        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res
        









"""
- loop through given array, extract the x and y co-rds, calculate euclidean distance, and add all 3 to a new array
- once all is done, turn array into a min heap
- create a res array, while k > 0, pop (min heap so it takes the lowest distance chars first) values into res, using only x+y
return res
"""