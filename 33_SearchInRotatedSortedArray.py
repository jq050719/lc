class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Two sorted segments are created after rotation
        # Use binary search to find the point at which the two segments meet (minimum element)
        index_of_min = self.find_index_of_minimum(nums)
        low, high = 0, len(nums) - 1
        # If target > nums[high], we need to check the left segment nums[0:index_of_min-1]
        if target > nums[high]:
            high = index_of_min - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1

        else:
            low = index_of_min
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1


    def find_index_of_minimum(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        # We want to find the point nums[i] s.t. nums[i-1] > nums[i]
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid-1] > nums[mid]:
                return mid
            # nums was originally ascending
            # Minimum is in right half of list if middle element greater than right most
            elif nums[mid] > nums[high]:
                low = mid + 1
            # Minimum is in left half of list if middle element less than left most
            elif nums[mid] < nums[low]:
                high = mid - 1
            # Otherwise, nums[low] <= nums[mid] <= nums[high]
            # Since nums was originally ascending, the minimum is just at index low
            else:
                return low
