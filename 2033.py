class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # convert into a list
        sorted_grid = []
        for row in grid:
            sorted_grid.extend(row)

        # sort list and obtain median element
        sorted_grid.sort()
        median = sorted_grid[len(sorted_grid) // 2]
        
        count = 0
        remainder = median % x
        for num in sorted_grid:
            if num % x != remainder:  # in this case, we cannot make num equal to the median
                return -1
            # otherwise, we can make num equal to the median
            # number of operations needed is |num - median| / x
            num_operations = abs(num - median) // x  # need to use integer division
            count += num_operations

        return count
        
