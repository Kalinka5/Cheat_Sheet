users_tuple = (
    ("+380991366764", "Roma"),
    ("+380661954882", "Danya"),
    ("+380985732641", "Alina")
)

gmails = {
    1: "dfgjhdfghjfdhg324432@gmail.com",
    2: "fjghjfdfd12@gmail.com",
    3: "danechka38@gmail.com"
}

gmails_2 = {
    4: "fdjhhjvcsdbhdsdsfb2134@gmail.com",
    5: "dfg213@gmail.com"
}

users = {
    "Eldar": {
        "phone": "+380503455297",
        "gmail": "eldarka2323@gmail.com"
    },
    "Roma": {
        "phone": "+380991256774",
        "gmail": "romochka567234@gmail.com"
    }
}

# Make dictionary from tuple
users_dict = dict(users_tuple)

# Get value by key
second_gmail = gmails[2]
# Method get() to get safely item value
some_gmail_1 = gmails.get(4)  # = None
some_gmail_2 = gmails.get(4, "We dont`t have this gmail!")  # = "We dont`t have this gmail!"
# Get value in complex dict
roma_phone = users["Roma"]["phone"]

# Change item value by key (or add in the end of dictionary).
gmails[3] = "klkjsdhfjdsaf222222@gmail.com"

# Remove item by key
gmails.pop(1)
gmails.pop(1, "We dont`t have this gmail!")
# Remove item by operator del
del gmails[1]
# Remove all items
gmails.clear()

# Copy all values to another variable
gmails_3 = gmails.copy()

# Combining Dictionaries
gmails.update(gmails_2)  # if keys are the same, second dict will replace first

# Enumeration of the dictionary
# by keys
for key in gmails:
    print(key)
for key in gmails.keys():
    print(key)
# by values
for value in gmails.values():
    print(value)
# by keys and values
for key, value in gmails.items():
    print(f"Place: {key}  Gmail: {value}")
