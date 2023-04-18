def find_duplicate(nums):
    verify_nums = all(isinstance(num, int)for num in nums)
    if not nums or not verify_nums or len(nums) < 2 or min(nums) < 1:
        return False

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

    return False
