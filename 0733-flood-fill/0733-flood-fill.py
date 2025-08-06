class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        colour = image[sr][sc]
        if colour == color:
            return image
        
        def dfs(r, c):
            if image[r][c] == colour:
                image[r][c] = color
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < row:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c + 1 < col:
                    dfs(r, c+1)

        dfs(sr, sc)
        return image