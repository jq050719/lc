class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        longest = 0
        for num in set_of_nums:
            # If num - 1 is in nums, then a sequence starting with num cannot be the longest sequence
            if num - 1 not in set_of_nums:
                seq = [num]
                while seq[-1] + 1 in set_of_nums:
                    seq.append(seq[-1] + 1)
                longest = max(longest, len(seq))

        return longest
        
