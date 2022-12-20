data_1 = ("Daniil", 19, "Amazon")
data_2 = ["Eldar", 19, "Binance"]

# Make tuple from list
eldar = tuple(data_2)

# Get item value
name = data_1[0]

# Tuple decomposition
name, age, company = data_1

# Make slices
not_name = data_1[1:]
unpaired_numbers = data_1[::2]
not_company = data_1[:2]
reversed_tuple = data_1[::-1]

# Get Item index
data_1.index(19)

# Get amount of current element
data_1.count("Amazon")
