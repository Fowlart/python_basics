list_from_range_1 = list(range(0,12,2))
print(list_from_range_1)

list_from_range_2 = [el for el in range(0,12,2)]
print(list_from_range_2)

reversed_list = list(range(10,0,-1))

print(reversed_list)

for i in range(10,0,-1):
    print(f"={i}=")

print("It is possible to identify a length of the range: ")
print(len(range(10,0,-1)))

# enumerate - accepts iterable, returns pairs with indexes
fruits = ['apple', 'banana', 'pear', 'orange']
for (index, fruit) in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")