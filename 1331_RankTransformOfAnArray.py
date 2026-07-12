class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_copy = arr.copy()
        arr_copy.sort()
        num_to_rank = {}
        rank = 1
        for i in range(len(arr_copy)):  # Iterate through sorted array, not the original
            num = arr_copy[i]
            if num not in num_to_rank:  # We see a new number
                num_to_rank[num] = rank
                rank += 1  # Increment rank since the next new number will be greater
            # If number already seen, do nothing

        res = [0] * len(arr)
        for i in range(len(arr)):
            res[i] = num_to_rank[arr[i]]

        return res
