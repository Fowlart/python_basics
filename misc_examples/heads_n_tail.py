from random import choice

n = input("please enter the number of coin flips: ")
my_range = range(int(n))
result = []
for i in my_range:
    result.append(choice(["head", "tail"]))

# Count the number of "head" in result
head_count = result.count('head')
tail_count = result.count('tail')

print("Number of heads: ", head_count)
print("Number of tails:", tail_count)