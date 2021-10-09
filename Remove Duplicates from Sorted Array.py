def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        ulen = 0
        unique = None
        for i in range(len(nums)):
            if nums[i] != unique:
                unique = nums[i]
                nums[i] = None
                nums[ulen] = unique
                ulen += 1
            else:
                nums[i] = None
        return ulen
