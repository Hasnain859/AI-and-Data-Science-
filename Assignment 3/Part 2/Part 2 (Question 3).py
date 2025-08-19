# Initial list
fruits = ["apple", "raspberry", "pineapple", "cherry"]

# a. Check if "apple" is present and get its index
if "apple" in fruits:
    apple_index = fruits.index("apple")
    print(f"'apple' is present at index {apple_index}")
else:
    print("'apple' is not present in the list")

# b. Replace "raspberry" and "pineapple" with "orange"

fruits[1:3] = ["orange"]
print("After replacing raspberry and pineapple with orange:", fruits)

# c. Insert "apricot" at index 2
fruits.insert(2, "apricot")
print("After inserting apricot at index 2:", fruits)

# d. Extend the list with ["car", "bike", "aeroplane"]
fruits.extend(["car", "bike", "aeroplane"])
print("After extending the list:", fruits)
