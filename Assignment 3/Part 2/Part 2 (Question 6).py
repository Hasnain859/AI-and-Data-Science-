Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

# a. Separate strings and numbers
strings = [item for item in Gadgets if isinstance(item, str)]
numbers = [item for item in Gadgets if isinstance(item, (int, float))]

print("Strings list:", strings)
print("Numbers list:", numbers)

# b. Sort strings ascending and descending (alphabetically)
strings_asc = sorted(strings)
strings_desc = sorted(strings, reverse=True)

print("Strings ascending:", strings_asc)
print("Strings descending:", strings_desc)

# c. Sort strings by length of elements
strings_sorted_by_length = sorted(strings, key=len)
print("Strings sorted by length:", strings_sorted_by_length)

# d. Sort numbers ascending and descending
numbers_asc = sorted(numbers)
numbers_desc = sorted(numbers, reverse=True)

print("Numbers ascending:", numbers_asc)
print("Numbers descending:", numbers_desc)
