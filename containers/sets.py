set_1: set = {"one", "two", "tree"}
set_2: set = {"4", "5", "6", "one"}
set_3: set = set_1 & set_2
print(set_1)
print(set_2)
print(set_3)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8, 9, 10}
print(f"intersection: {set_a.intersection(set_b)}")
print(f"difference: {set_a.difference(set_b)}")
print(f"difference: {set_b.difference(set_a)}")
print(f"symmetric_difference: {set_a.symmetric_difference(set_b)}")

# difference with the list
print(set_a.difference([4, 5, 6, 7]))
