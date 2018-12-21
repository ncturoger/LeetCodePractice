def bubble_sort(nums):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            print(nums)

bubble_sort([9,8,7,6,5,4,3,2,1])

    