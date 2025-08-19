numbers = [32, 54, 66, 11, 77, 10, 90]

# a. Remove items less than 20
numbers = [num for num in numbers if num >= 20]
print("After removing items less than 20:", numbers)

# b. Sort ascending and descending
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)

# c. Compute average value
average = sum(numbers) / len(numbers) if numbers else 0
print("Average value:", average)
