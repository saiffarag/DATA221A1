def cumulativePercentage(nums):
    total = len(nums) # Number of items in the list
    result = {}  # Create result dictionary

    for key in sorted(set(nums)): # Loop through each unique number in nums, sorted in ascending order
        count = 0 
        for n in nums: # Count how many numbers in nums are less than or equal to key
            if n <= key:
                count += 1

        result[key] = (count / total) * 100 # Compute cumulative percentage and store in dictionary

    print(result)         

nums = [3, 1, 2, 3, 4, 2]
cumulativePercentage(nums)
