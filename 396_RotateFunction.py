class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(0) is original list
        # F(1) shifts all elements right. Last element moves to front
        # F(len(nums)) is just the original list
        # How does F(k) change from F(k-1)?
        # Note: F(k) = sum(nums) + F(k - 1) - (n * element with coefficient n - 1 in F(k - 1))
        # F(0): element with coefficient n - 1 is last element in original list --> n-1
        # F(1): element with coefficient n - 1 is second last element in original list --> n-2
        # F(k): element with coefficient n - 1 is at index (n - 1 - k) in original list
        # n - 1 - k is always a valid index because 1 <= k <= n-1

        # The element with coefficient n - 1 in F(k - 1) is n - 1 - (k - 1) = n - k

    
        max_so_far = self.rotation_function(nums)  # find F(0)
        sum_of_list = sum(nums)  # we need this to find F(k)
        prev = max_so_far  # we need to keep track of F(k - 1) to find F(k)
        n = len(nums)

        for k in range(1, n):
           index_of_last = n - k  # get index of last element for F(k-1)
           res = sum_of_list + prev - (n * nums[index_of_last])  # compute F(k)
           max_so_far = max(max_so_far, res)
           prev = res  # current F(k) becomes next F(k-1)

        return max_so_far



    # Helper function to find F(0)
    def rotation_function(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            res += i * nums[i]

        return res
        
