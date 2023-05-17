nums = [1,3,5,6]
target = 7
for i in nums:
    if target == i:
        print(nums.index(i))
        break
    elif target > i and target < nums[nums.index(i)+1]:
        print(nums.index(i) + 1)
        break
