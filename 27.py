def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    
    # Fill the remaining part of the array with underscores for clarity (though it's not required)
    for k in range(i, len(nums)):
        nums[k] = "_"
    
    return i

# Example usage:
nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = removeElement(nums, val=2)

# Output the results
print("k =", k)  # The number of elements remaining after removal
print("nums =", nums)  # The modified list
    
