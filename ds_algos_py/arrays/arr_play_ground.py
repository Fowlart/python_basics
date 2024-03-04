# removing an element
ran_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del ran_arr[4]
print(ran_arr)

# wrong way to remove
ran_arr[0] = None
print(ran_arr)

# the type of '[]' is <class 'list'>
# the list from Python is the same as ArrayList from Java
print(type(ran_arr))

# storing objects in array:
obj_arr = [{"name": "John", "age": 23}, {"name": "Alice", "age": 24}, {"name": "Arthur", "age": 25}]
print(obj_arr[0].get("name"))
print(type(obj_arr[0]))

