class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        new_mat = []

        for row in mat:
            for num in row:
                flatten.append(num)

        if r*c != len(flatten):
            return mat
        else:
            for row_idx in range(r):
                new_mat.append(flatten[row_idx * c : row_idx * c + c])
            return new_mat