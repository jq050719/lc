class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # 90 degree clockwise rotation: Transpose matrix and reverse rows
        m = len(boxGrid)
        n = len(boxGrid[0])
        newBoxGrid = [[boxGrid[j][i] for j in range(m)] for i in range(n)]

        # Note: Now n = len(newBoxGrid) and m = len(newBoxGrid[i])
        for i in range(n):
            newBoxGrid[i].reverse()

        # Iterate down each column
        # If newBoxGrid[i][j] is '#' and newBoxGrid[i+1][j] is '.', swap them
        for j in range(m):
            num_swaps = 1
            while num_swaps > 0:
                num_swaps = 0
                for i in range(n-1):
                    if newBoxGrid[i][j] == '#' and newBoxGrid[i+1][j] == '.':
                        newBoxGrid[i][j], newBoxGrid[i+1][j] = newBoxGrid[i+1][j], newBoxGrid[i][j]
                        num_swaps += 1

        return newBoxGrid
        
