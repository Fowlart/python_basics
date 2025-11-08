
if __name__ == "__main__":

    # the list
    # mutable, ordered
    print("__________the list_________")
    the_list: list = ["one", 2, 3.14]
    # main methods:
    the_list.append("4")
    print(the_list)
    the_list.insert(0, 0)
    the_list.insert(0, -1)
    print(the_list)
    the_list.remove('one')
    print(the_list)
    try:
        the_list.sort()
        print(the_list)
    except Exception as s:
        print(s)
    print(f"the index of element: {the_list.index('4')}") # 4
    print(f"the index of element: {the_list.index(0)}") # 1

    # the tuple
    # ordered, immutable
    print("__________the tuple_________")
    the_tuple: tuple = (1,"one",1,"two",2,"three","3","one")
    print(f"tuple: {the_tuple}")
    print(f"count of elements: {the_tuple.count('one')}")
    print(f"index of `3`: {the_tuple.index('3')}")
    the_tuple = the_tuple + ("yet another element",)
    print(f"the tuple: {the_tuple}")

    # sets
    # uniqueness of elements, mutability, unordered
    print("__________the set_________")
    the_set_a = set()
    the_set_a.add(1)
    the_set_a.add(2)
    the_set_a.add("tree")
    the_set_a.add("four")
    the_set_a.add(5)
    the_set_a.add("common")

    the_set_b = {10, 11, 12, 13, "common", 5}
    the_set_a.remove("tree")

    print(f"the set a: {the_set_a}")
    print(f"the set b: {the_set_b}")

    print(f"union: {the_set_a.union(the_set_b)}")
    print(f"intersection: {the_set_a.intersection(the_set_b)}")
    print(f"difference: {the_set_a.difference(the_set_b)}")

    # the dict
    print("__________the dict_________")
    my_dict = {0:"knife",
               1:"flashlight",
               2:"smart-phone",
               3:"wallet",
               "main":"gun"}

    print(my_dict)
    print(f" Main item: {my_dict['main']}")
    print(f" 1 item: {my_dict[1]}")
    print(f" Main item: {my_dict.get('main')} ") #
    main_value = my_dict.pop('main')
    print(f" Main value from dict removed: {main_value}")
    print(f" Dict after removing {my_dict}")
    print(' Views from dict: ')
    print(my_dict.keys())
    print(my_dict.values())
    print(my_dict.items())
    #practical usage of object-view
    print(1 in my_dict.keys())
    print(10 in my_dict.keys())

    # will cause error
    # print(my_dict[10])

    # will not cause error
    print(my_dict.get(10))

    if 10 in my_dict.keys():
        print(my_dict.get(10))


