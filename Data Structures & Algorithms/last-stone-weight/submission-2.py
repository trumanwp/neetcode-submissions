import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if largest > second:
                heapq.heappush_max(stones, largest - second)

        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        
            




"""
- array of stones, each num represents weight of a stone

we want to run simulation on the stones
at each step:

- take 2 heaviest stones, weight x and y
- if x==y, both are destroyed
- if x < y, x is destroyed, and y has new weight of y - x

- Return the weight of the last remaining stone, or 0 if none remain

----------------------
"""

"""
SOLUTION


- use maxheap
- x is the root, y is the largest child
- if x == y, heappop 2x
- if y > x, heappop 1x, but value of y becomes y - x
- continue
- 

"""