class Solution:
        
    def minSwap(self, arr, k): 
        n = len(arr)
        
        # Step 1: Count elements <= k
        good = sum(1 for x in arr if x <= k)
        
        # Step 2: Count bad elements in first window
        bad = sum(1 for i in range(good) if arr[i] > k)
        
        ans = bad
        
        # Step 3: Slide the window
        i = 0
        j = good
        
        while j < n:
            # Remove left element
            if arr[i] > k:
                bad -= 1
            
            # Add right element
            if arr[j] > k:
                bad += 1
            
            ans = min(ans, bad)
            
            i += 1
            j += 1
        
        return ans
