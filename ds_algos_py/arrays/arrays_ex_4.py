# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from \
# a user using input() function

max_num = input("Enter a number: ")
result = []
for num in range(int(max_num)):
    if num % 2 == 0:
        result.append(num)
print(result)
