class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # array height
        # each val in height is a vertical line in a graph
        # need to find the highest area 
        # x value = i[right] - i[left]
        # y value = lower of the 2 values in h

        # 2 pointer
        # take min height out of the 2, multiply by x value difference to get area
        # store area in "highest"
        # move lower of the 2 values in, recalculate area
        # continue doing this, return the highest value

        left = 0
        right = len(heights) - 1
        highest = 0

        while left < right:
            volume = min(heights[left], heights[right]) * (right-left)
            highest = max(highest, volume)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        
        return highest