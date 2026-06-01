class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # The most expensive candy that can be taken for free is the 3rd most
        # We are forced to buy the 1st and 2nd most expensive candies anyway
        # After the 3rd most, the next most expensive we can take is the 6th most

        # Sort cost from high to low
        cost.sort()
        cost.reverse()
        
        res = 0
        for i in range(len(cost)):
            # We can take candies that are a multiple of 3 (3rd most, 6th most, etc.)
            # This corresponds to indices 2, 5, 8, etc.
            # So, we need i % 3 == 2 to take for free
            # If, i % 3 != 2, we can't take for free
            if i % 3 != 2:
                res += cost[i]

        return res
        
