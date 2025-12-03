# Exercise 1
# Find the average of the digits of a given number
def average_of_digits(num):
    total = 0
    count = 0
    n = num

    while n > 0:
        digit = n % 10
        total += digit
        count += 1
        n //= 10

    return total / count


# Exercise 2
# Find the product of the smallest and largest digits of a given number
def product_smallest_largest(num):
    n = num
    smallest = 9
    largest = 0

    while n > 0:
        digit = n % 10
        if digit < smallest:
            smallest = digit
        if digit > largest:
            largest = digit
        n //= 10

    return smallest * largest


# Exercise 3
# Count digits divisible by 3
def count_digits_divisible_by_3(num):
    n = num
    count = 0

    while n > 0:
        digit = n % 10
        if digit % 3 == 0:
            count += 1
        n //= 10

    return count


# Exercise 4
# Find and return reverse of a number
def reverse_number(num):
    n = num
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return rev
