#  ::: String Concatenation
# first_name = "subomi"
# age = 18

# print("How are you " + first_name)

# print("How are you " + first_name + " " + "?")

# but for our age we have to cast it back to a string since its an integer beacuse you can only concatenate strings
# print("How are you " + first_name + "and i am " + str(age) + " years old")

# argument by position
# print('{},{}'.format(first_name,age))

# argument by name 
# print('my name is {firstname} and i am {age} years old'.format(firstname=first_name, age=age))

# f - string 
# print(f'my name is {first_name} an i am {age} years old')

# ::: String Methods
# first_name = "subomi"

# print(first_name.capitalize())
# What it does: Makes the first letter of first_name uppercase, and the rest lowercase.
# Example: If first_name = "dAVid", this will print David.
# Why useful: Good for making names look neat in output.

# print(first_name.count('a'))
# What it does: Counts how many times the letter 'a' appears in first_name.
# Example: If first_name = "amanda", this will print 3.
# Why useful: Helpful for finding frequency of characters.

# print(len(first_name))
# What it does: Finds the length of the string — basically, how many characters are in first_name.
# Example: If first_name = "John", this will print 4.
# Why useful: Useful when you need to know the size of the string (for loops, limits, etc.).

# print(first_name.swapcase())
# What it does: Swaps the case of each letter — uppercase becomes lowercase, lowercase becomes uppercase.
# Example: "DaViD" becomes "dAvId".
# Why useful: Can be used for stylistic text changes or case-flipping logic.

# print(first_name.startswith('d'))
# What it does: Checks if first_name starts with the letter 'd'.
# Returns: True or False.
# Example: "daniel" → True, "Samuel" → False.
# Why useful: Often used for filtering strings that match a certain pattern.

# print(first_name.replace(first_name, "obans"))
# What it does: Replaces the entire string first_name with "obans".
# Example: If first_name = "David", it will print "obans".
# Why useful: This is a bit of an odd usage — normally .replace() is used to change part of a string, but here you’re replacing the whole thing.
