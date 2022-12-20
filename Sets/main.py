girls = {"Katya", "Nika", "Diana", "Katya"}
girls_2 = {"Lera", "Vika", "Sasha", "Nika", "Diana"}
girls_3 = {"Katya", "Nika", "Diana", "Lera", "Sasha"
           }
# Set has only unique values
print(girls)  # = "Katya", "Nika", "Diana"

# Add item to the end
girls.add("Adele")

# Remove item by value with error
girls.remove("Alice")
# Remove item by value without error
girls.discard("Alice")
# Remove all items
girls.clear()

# Copy all values to another variable
fruits_2 = girls.copy()

# Enumeration of the sets by indexes and values
for index, fruit in enumerate(girls):
    print(f"{index}: {fruit}")

# Methods
# combines two sets
print(girls.union(girls_2))  # = "Katya", "Nika", "Diana", "Lera", "Vika", "Sasha"
print(girls | girls_2)  # = "Katya", "Nika", "Diana", "Lera", "Vika", "Sasha"
# elements that are in both sets
print(girls.intersection(girls_2))  # = "Nika", "Diana"
print(girls & girls_2)  # = "Nika", "Diana"
# elements that are in first set, but missing in second set.
print(girls.difference(girls_2))  # = "Katya"
print(girls - girls_2)  # = "Katya"
# get set without common elements
print(girls.symmetric_difference(girls_2))  # = "Katya", "Lera", "Vika", "Sasha"
print(girls ^ girls_2)  # = "Katya", "Lera", "Vika", "Sasha"
# is first set subset to second set
girls.issubset(girls_3)  # True
girls.issubset(girls_2)  # False
# is first set superset to second set
girls_3.issuperset(girls)  # True
girls.issuperset(girls_3)  # False
