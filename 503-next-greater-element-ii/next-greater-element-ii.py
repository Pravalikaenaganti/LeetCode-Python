class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(1, n):
                if nums[(i + j) % n] > nums[i]:
                    res[i] = nums[(i + j) % n]
                    break
        return res
