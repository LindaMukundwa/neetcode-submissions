class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left = 0
        window_sum = 0
        
        for right in range(len(arr)):  # Use index, not value
            window_sum += arr[right]  # Add to running sum
            
            # Only check when window is exactly size k
            if right - left + 1 == k:
                if window_sum / k >= threshold:
                    count += 1
                # Slide window
                window_sum -= arr[left]
                left += 1
        
        return count