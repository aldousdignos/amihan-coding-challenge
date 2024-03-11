def lenghtOfLIS(arr):
    LIS = [1] * len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    
    return max(LIS)

# Example usage
# arr = [10, 9, 2, 5, 3, 7, 101, 18]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lenghtOfLIS(arr)) # Output: 4