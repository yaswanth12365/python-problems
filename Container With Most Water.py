class Solution:
    def maxArea(self, height: List[int]) -> int:
        #holds maximum area of water
        maxWater = 0
        
        #two pointers, one starting at index 0, other at last index of the list
        left_pointer, right_pointer = 0, len(height) - 1
        
        #iterate through until both left and right are one away from each other
        while left < right:
            maxWater = max(maxWater, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
            
            #increasing whichever pointer has a smaller line, we want to maximize the area
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return maxWater
