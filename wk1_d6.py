my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, None]

# Print Checks
print("List:", my_list)
print("List element at index 0:", my_list[0])

# Slice Assignments (Replacing and Adding Elements)
temp_list = ["a", "b", "c"]
temp_list[1:3] = ["water", "break"]  # replace index 1 and 2
temp_list[1:2] = ["water", "break"]  # replace index 1 and insert one
temp_list[1:2] = ["break"]  # replace index 1

# Adding & Extending Elements
my_list.append(6)  # Adds 6 to the very end
my_list.insert(2, 99)  # Inserts 99 at index 2, shifts rest right
my_list.extend([7, 8])  # add items from iterable
my_list.extend([9, 10])  # add more items
print("After append and extend:", my_list)

# Deleting Elements
my_list.pop(3)  # Removes and returns item at index 3
my_list.remove(2)  # Removes first occurrence of the value 2
my_list.clear()  # Empties the entire list
del my_list  # Completely deletes the list variable from memory

# Sorting and Reversing
sort_list = [3, 1, 4, 1, 5, 9]
sort_list.sort()  # Sorts in place (ascending)
sort_list.sort(reverse=True)  # Sorts in place (descending)
# Example for case-insensitive sorting (only for string lists)
string_list = ["banana", "Apple", "cherry"]
if all(isinstance(x, str) for x in string_list):
    string_list.sort(key=str.lower)
sort_list.reverse()  # Reverses layout of elements in place

# List Comprehensions
squares = [i * i for i in range(1, 9)]
long_names = [name for name in ["Ram", "Hari", "SitaMax"] if len(name) > 5]


my_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "world", 3.14, False)

print("\nTuple:", my_tuple)
print("Tuple element at index 1:", my_tuple[1])
# my_tuple[0] = 10  # ERROR: Tuples cannot be modified after creation

# Swapping Variables Using Tuple Mechanics
a, b = 10, 20
a, b = b, a  # Directly swaps values without a temp variable

# Tuple Unpacking
tup = (1, 23, 44)
x, y, z = tup  # Extracts items into matching variables
print("Unpacked Tuple:", x, y, z)


my_set = {1, 2, 3, 4, 5}
set_from_list = set([1, 2, 2, 3, 3, 4])  # Converts list & removes duplicates

print("\nSet:", my_set)
print("Set from list:", set_from_list)

# Modifying Sets
my_set.add(6)  # Adds a single element
my_set.update([7, 8, 9])  # add multiple elements
my_set.remove(6)  # remove 6
print("After add and update:", my_set)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union (|):", set1 | set2)  # All unique items from both sets
print("Intersection (&):", set1 & set2)  # Only items present in both sets
print("Difference (-):", set1 - set2)  # Items in set1 that are not in set2


my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("\nDictionary:", my_dict)

# Accessing Data
print("Value by key:", my_dict["name"])  # Raises KeyError if key doesn't exist
print("Safe access:", my_dict.get("name"))  # Returns None if key doesn't exist
print("Keys view:", my_dict.keys())
print("Values view:", my_dict.values())
print("Items view:", my_dict.items())  # Returns view of (key, value) tuples

# Adding, Updating & Merging
my_dict["country"] = "USA"  # Adds a single new key-value pair
my_dict.update(
    {
        "email": "alice@example.com",
        "age": 26,
    }
)  # Updates multiple keys
print("After adding and updating:", my_dict)

# Deleting Data
my_dict.pop("age")  # Removes specified key and returns its value
my_dict.popitem()  # Removes and returns last inserted key-value pair
del my_dict["city"]  # Deletes specific key-value pair from memory
my_dict.clear()  # Empties the entire dictionary

# Nested Dictionary Example
contacts = {
    "Ram": {"phone": "9800000000", "email": "ram@gmail.com"},
    "Hari": {"phone": "9811111111", "email": "hari@gmail.com"},
}
print("Nested element access:", contacts["Ram"]["phone"])

# Dictionary Comprehension
square_dict = {i: i * i for i in range(1, 6)}


print("\nType Checking:")
# Exact type matching
print("Type of list:", type([1, 2]))
print("Type of tuple:", type((1, 2)))
print("Type of set:", type({1, 2}))
print("Type of dict:", type({"a": 1}))

# Preferred inheritance-friendly type check (isinstance)
check_list = [1, 2, 3]
check_tuple = (1, 2, 3)
check_set = {1, 2, 3}
check_dict = {"a": 1}

print("Is a list?", isinstance(check_list, list))
print("Is a tuple?", isinstance(check_tuple, tuple))
print("Is a set?", isinstance(check_set, set))
print("Is a dict?", isinstance(check_dict, dict))
