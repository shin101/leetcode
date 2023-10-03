from typing import List
# 84. Largest Rectangle in Histogram
# Hard

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# initiate stack (store idx, height)
# iterate through i, h in heights array
# pop if last item on stack is taller than current height
 


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair : (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h : 
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea