class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        num_left, num_right, num_either = 0, 0, 0
        for char in moves:
            if char == 'L':
                num_left += 1
            elif char == 'R':
                num_right += 1
            # char == '_'
            else:
                num_either += 1
        
        # choose num_either to be the larger of L and R
        if num_left > num_right:
            num_left += num_either
        else:
            num_right += num_either
        
        return abs(num_right - num_left)
        
