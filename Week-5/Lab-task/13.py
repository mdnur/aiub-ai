def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


numbers = [3, 6, 8, 2, 5, 9, 10, 11]
even_count, odd_count = count_even_odd(numbers)
print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)