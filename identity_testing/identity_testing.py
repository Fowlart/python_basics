a = [1, 2, 3]
b = [1, 2, "a"]
c = a
print(a == b)  # False
print(f"{a} => {id(a)}")
print(f"{b} => {id(b)}")
print(f"{c} => {id(c)}")
print(f"syntax suger identity check a is c: {a is c}")  # True
print(a is not b)
a[2] = "a"
print(a == b)  # True because contains the same values

random_str_1 = "Brown fox jumped over the lazy frog"
random_str_2 = "Brown fox jumped over the lazy frogs"
print(random_str_1 is random_str_2)
