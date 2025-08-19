student_data = ["Tahir", 44, "AI and Data Science", True]

strings = []
numbers = []
booleans = []

for item in student_data:
    if isinstance(item, str):
        strings.append(item)
    elif isinstance(item, (int, float)) and not isinstance(item, bool):
        numbers.append(item)
    elif isinstance(item, bool):
        booleans.append(item)

print("Strings:", strings)
print("Numbers:", numbers)
print("Booleans:", booleans)
