def cumulativePercentage(nums):
    total = len(nums)
    result = {}
    
    for key in sorted(set(nums)):
        count = 0
        for n in nums:
            if n <= key:
                count += 1
        result[key] = (count / total) * 100

    print(result)

nums = [3, 1, 2, 3, 4, 2]
cumulativePercentage(nums)