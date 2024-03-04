init_num: int = int(input("Please enter number: "))
my_list = [init_num]
for i in range(init_num):
    num = input("Please enter number: ")
    my_list.append(num)
print(my_list)