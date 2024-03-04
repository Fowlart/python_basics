small_int_1 = int("100")
small_int_2 = int("100")
print(small_int_1 is small_int_2)
small_int_1 = int("100000000")
small_int_2 = int("100000000")
print(small_int_1 is small_int_2)
print(id(small_int_1))
print(id(small_int_1))

a = 1404991071833123
b = 1404991071833123
print(a is b)
print(a == b)
print(id(a) is id(b))
print(id(a) == id(b))
print(type(id(a)))
a = b
b = 11
print(a is b)

a = [1, 2, 3]
b = a
a = [1, 2, 3]

print(a is b)

one_ancstor = "one ancstor"
other_ancestor = "other ancestor"

# Calculate the identity of a new alien here
new_alien = (id(one_ancstor) + id(other_ancestor))/2
print(new_alien)
