from my_march_linked_list.MyLinkedList import MyLinkedList

if __name__ == "__main__":
    # code to run the tests
    linked_list = MyLinkedList()
    linked_list.append(1)
    linked_list.add_at_tail(2)
    linked_list.add_at_tail(3)

    linked_list.add_at_head(0)
    linked_list.add_at_tail(4)

    linked_list.add_at_index(0, "start")
    linked_list.add_at_index(linked_list.length(), "end")
    # linked_list.add_at_index(10,"end_end_end")

    # linked_list.delete_at_index(1)
    # linked_list.delete_at_index(2)
    # linked_list.delete_at_index(3)

    print(linked_list)
    print(f"Length of linked_list: {linked_list.length()}")

    linked_list.replace_all_values(["one", "two", "three", "four", "five"])

    print(linked_list)
    print(f"Length of linked_list: {linked_list.length()}")

    # iterable test
    for i in linked_list:
        print(i)

    print("three" in linked_list)

    # delete head %)
    print(linked_list)
    linked_list.delete_at_index(0)
    print(linked_list)
