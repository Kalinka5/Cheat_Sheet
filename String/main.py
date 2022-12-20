# make single or double quotes in string
text_1 = "I want laptop \"Macbook\"!"

# Make new line
text_2 = "Danya said:\n- I`m 19 years old."

# Make tab (4 spaces)
text_3 = "\tEnding..."

# Symbol “r” to make path without special symbols (\n, \t)
path = r"C:\Daniil\Python"

# Remove items in string
text_4 = "<ksdjhfjbdjfbdsbfsdb@gmail.com>"
text_without_parentheses = text_4[1:-1]

# String concatenation as “f” format
first_name = "Daniil"
second_name = "Kalinevych"
age = 19
full_name = f"{first_name} {second_name}. Age: {age}"

# String repeating
text = 'Dan'
print(f"{text:#>20}")  # = #################Dan
print(f"{text:#<20}")  # = Dan#################
print(f"{text:#^20}")  # = ########Dan#########

# String comparison
"1A" < "1a" < "2a" < "Aa" < "aa"

# Make lower or upper case string
text_5 = "AhjjhhACBHBFHGrigjiurgOU"
lower_text = text_5.lower()
upper_text = text_5.upper()

# convert initial characters in all words to upper case
text_6 = "daniil kalinevych"
print(text_6.title())  # = Daniil Kalinevych

# convert first initial character to upper case
text_6 = "daniil is a leader in our group!"
print(text_6.capitalize())  # = Daniil is a leader in our group!

# From string get int format Unicode
char = 'A'
print(ord(char))  # = 65

# Get amount of all elements in the string
text_6 = "Hello, my name is Rodrigo!"
print(len(text_6))  # 26

# CHECKING
# Check is word in string (True or False)
text_7 = "mom, dad, brother"
print("mom" in text_7)  # = True
print("sister" in text_7)  # = False

# Check has string only alphabet symbols
text_8 = "Programmer"
print(text_8.isalpha())  # = True

# Check has string only integer symbols
nums = "2334123"
print(nums.isdecimal())  # = True
print(nums.isdigit())  # = True
print(nums.isnumeric())  # = True

# Check is string in lowercase
name = "andrew"
name_2 = "Andrew"
print(name.islower())  # = True
print(name_2.islower())  # = False

# Check is string in uppercase
name_3 = "ANDREW"
name_4 = "ANDREw"
print(name_3.isupper())  # = True
print(name_4.isupper())  # = False

# Check is string starts with a word, or a letter
text_8 = "I have a breakfast this morning."
print(text_8.startswith("I"))  # = True

# Check is string ends with a word, or a letter
print(text_8.endswith("morning"))  # = True

# Remove spaces on the left side
text_9 = "        Hi"
text_9.lstrip()

# Remove spaces on the right side
text_10 = "Hi        "
text_10.rstrip()

# Remove spaces on the both side (left and right)
text_11 = "         Hi      "
text_11.strip()

# Get index of the char (if it doesn't find char, you get -1)
text_12 = "My name is Daniil"
print(text_12.find("n"))  # = 3

# Make replace an old substring to a new substring
text_13 = "My name is Roma"
text_13 = text_13.replace("Roma", "Daniil")

# Splits a string into substrings depending on the delimiter
text_14 = "Danya, Roma, Katya, Nika"
names = text_14.split(", ")  # = ["Danya", "Roma", "Katya", "Nika"]

# Join substrings into a string inserting a separator between them
text_15 = ["Danya", "Roma", "Katya", "Nika"]
names_2 = ", ".join(text_15)  # = "Danya, Roma, Katya, Nika"
