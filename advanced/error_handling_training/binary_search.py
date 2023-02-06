# binary search works only on

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid

        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return 'not in the provided list'


nums = [int(x) for x in input().split(', ')]
target_value = int(input())
result = binary_search(nums, target_value)
print(f'The target value index is: {result}')