# Lists []

fruits = ['apple', 'banana', 'cucumber', 'carrot', 'pawpaw']

number = [1,2,3,4,5,6]

mixing = ['apple', 1,2,3,3.7, True]

# fruits → list of strings.
# number → list of integers.
# mixing → list with different data types (string, int, float, boolean).

print(fruits)
print(number)
print(mixing)

# get a value
print(fruits[1])
# Lists use zero-based indexing.
# fruits[1] gets the second item in the list (banana).

# get the length of the list
print(len(fruits))
# len() returns the number of items in the list.

# List methods
fruits.append(1)
print(fruits)
# Adds the given element to the end of the list.
# Here, the number 1 was added.

fruits.remove('apple')
print(fruits)
# Removes the first matching item from the list.

fruits.insert(2, 'cashew')
print(fruits)
# insert(index, value) puts an item at a specific position without replacing others.

fruits.pop(4)
print(fruits)
# Removes and returns the item at the given index.
# If no index is given, it removes the last item.

fruits.reverse()
print(fruits)
# Changes the order of items to be backwards.

fruits.sort()
print(fruits)
# Sorts the list in ascending order.
# Works for numbers or strings separately, but will give an error if the list has mixed data types.
