class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in mapping and mapping[j] != i:
                return [i, mapping[j]]
        
