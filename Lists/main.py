fruits = ["apple", "banana", "orange"]
fruits_2 = ["avocado", "grapefruit"]

# Get item value
apple = fruits[0]

# Change item value
fruits[2] = "kiwi"

# Add item to the end
fruits.append("cherry")
# Add item by index
fruits.insert(2, "Grapes")
# Add set items
fruits.extend(fruits_2)

# Combining Lists
fruits_3 = fruits + fruits_2

# Remove item by value
fruits.remove("apple")
# Remove item by index
fruits.pop(1)
# Remove all items
fruits.clear()
# Remove item by operator del
del fruits[1]
del fruits[:2]
del fruits[1:]

# Get last element
last = fruits[-1]

# List decomposition
apple, banana, orange = fruits

# Get Item index
fruits.index("banana")

# Get amount of current element
fruits.count("orange")

# Get reversed list
fruits.reverse()

# Get amount of all elements in the list
len(fruits)

# Get min and max value in the list
min(fruits)
max(fruits)

# Copy all values to another variable
fruits_4 = fruits.copy()

# Make sort list (by length, make reverse)
fruits.sort(key=len, reverse=True)
# Make sort new list
fruits_5 = sorted(fruits)

# Make slices
not_first = fruits[1:]
unpaired_numbers = fruits[::2]
not_last = fruits[:2]
reversed_list = fruits[::-1]

# Enumeration of the dictionary by indexes and values
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
