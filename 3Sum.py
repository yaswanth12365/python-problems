class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    s.add((nums[i], nums[left], nums[right]))
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return [list(i) for i in s]
