class Solution:
    def rotate(self, arr: List[int], d: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        d = d % n
        temp = []

        for i in range(n - d, n):
            temp.append(arr[i])

        for i in range(n - d - 1, -1, -1):
            arr[i + d] = arr[i]

        for i in range(d):
            arr[i] = temp[i]

        return arr
        
        


        