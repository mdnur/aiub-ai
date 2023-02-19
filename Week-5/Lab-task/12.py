"""Write a Python function (user defined/not built-in) to find the maximum and minimum numbers from a sequence of numbers."""


def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None
    else:
        max_num = max(numbers)
        min_num = min(numbers)
        return max_num, min_num
    
    
numbers = [10, 5, -3, 8, 2, 0, 4]
max_num, min_num = find_max_min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)