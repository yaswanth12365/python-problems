    def pivotIndex(self, nums):
		'''prefix sum, TC: O(2n)=O(n), SC: O(1)'''
        prefix_sum = 0
        total_sum = sum(nums) #O(n)
        for i in range(len(nums)): #O(n)
            prefix_sum = prefix_sum+nums[i]
            if prefix_sum==(total_sum+nums[i])/2:
                return i
        return -1
