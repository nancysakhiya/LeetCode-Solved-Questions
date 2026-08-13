class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        return arr

    def rotate(self, arr: List[int], d: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        d = d % n

        self.reverse(arr, 0, n - 1)
        self.reverse(arr, 0, d - 1)
        self.reverse(arr, d, n - 1)

