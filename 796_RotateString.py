class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # return False if len(s) != len(goal)
        if len(s) != len(goal):
            return False
        # If lengths are the same, then check if goal is a substring is s + s
        return goal in s + s
        
