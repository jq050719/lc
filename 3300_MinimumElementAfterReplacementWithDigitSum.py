class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = str(nums[i])
            res = 0
            for c in s:
                res += int(c)
            nums[i] = res

        return min(nums)
        
