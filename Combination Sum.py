class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		queue = deque([])

		for idx, val in enumerate(candidates):
			queue.append((idx, val, [val]))

		result = []

		self.bfs(candidates, queue, target, result)

		return result

	def bfs(self, nums, queue, target, result):
		while queue:
			idx, curSum, curPath = queue.popleft()
			# print(curPath)
			if curSum>target: continue

			if curSum == target:
				result.append(curPath)

			if curSum<target:
				for i in range(idx, len(nums)): # to remove duplicates, eg. [2,3,1] and [1,3,2] are the same since its combinations
					queue.append((i, curSum+nums[i], curPath+[nums[i]]))
