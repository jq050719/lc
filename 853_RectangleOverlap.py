class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # x1 = left edge, y1 = bottom edge, x2 = right edge, y2 = top edge
        rec1_left, rec1_bottom, rec1_right, rec1_top = rec1[0], rec1[1], rec1[2], rec1[3]
        rec2_left, rec2_bottom, rec2_right, rec2_top = rec2[0], rec2[1], rec2[2], rec2[3]

        # If bottom edge of rec1 touches or is above top edge of rec2, no overlap (and vice versa)
        if rec1_bottom >= rec2_top or rec2_bottom >= rec1_top:
            return False

        # If left edge of rec1 touches or is further right than right edge of rec2, no overlap (and vice versa)
        if rec1_left >= rec2_right or rec2_left >= rec1_right:
            return False

        return True
        
