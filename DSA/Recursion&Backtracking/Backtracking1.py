def permute(nums):
    result = []
    backtrack(nums, [], result)
    return result

def backtrack(nums, path, result):
    # Base case: If path contains all elements from nums, add it to result
    if len(path) == len(nums):
        result.append(path)
        return
    
    # Iterate over each element in nums
    for num in nums:
        # If num is not in the current path, append it and backtrack
        if num not in path:
            backtrack(nums, path+[num], result)


nums = [12, 24, 32]
print(permute(nums))
