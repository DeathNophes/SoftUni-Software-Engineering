def insertion_sort(nums):
    for i in range(1, len(nums)):   # We start from one because on 0 is sorted part
        key = nums[i]               # We take key because when shifting we lose it
        j = i - 1                   # We take the last value of sorted part

        # while we are not at the beginning and until we get to a position where we can put the key
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]   # We shift the elements
            j -= 1                  # We move left

        nums[j + 1] = key           # We put the key on the valid position


numbers = [int(x) for x in input().split()]
insertion_sort(numbers)
print(*numbers)

