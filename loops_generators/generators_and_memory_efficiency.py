# how much memory will take some var ?
import sys as s

some_string_1 = "Hello World!"
some_string_2 = "Bigger string! I am curious if you don't know, is the different strings has different size in bytes?"
char_size = "a"

print(s.getsizeof(some_string_1))

print(s.getsizeof(some_string_2))

print(s.getsizeof(char_size))

some_range = range(1, 1000000)

print(f"size of 'some_range' is {s.getsizeof(some_range)}")
print(f"the type of 'some_range' is {type(some_range)}")

# generator
def count_up_to(num: int):
    count = 0
    while count <= num:
        yield count
        count += 1


generator = count_up_to(1000000)

print(f"type of 'generator' is {type(generator)}")
print(f"the size of 'generator' is: {s.getsizeof(generator)}")

summary = 0
for i in generator:
    # print(f"the size of 'generator' is: {s.getsizeof(generator)}")
    # will always have 104 bytes
    summary = summary + i

print(f"the size of 'summary' is: {summary}")

