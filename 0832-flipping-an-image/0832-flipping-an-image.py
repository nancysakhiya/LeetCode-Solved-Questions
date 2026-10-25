class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        for row in image:
            l = 0
            r = len(row) - 1

            while l <= r:
                row[l], row[r] = 1 - row[r], 1 - row[l]
                l += 1
                r -= 1
        
        return image

        

