class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        min_len = n + 1
        curr_sum = 0
        start = 0

        for end in range(n):
            curr_sum += arr[end]

            # Shrink the window while sum is greater than x
            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1

        # If no valid subarray found
        return 0 if min_len == n + 1 else min_len
