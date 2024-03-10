from ds_algos_py.my_march_linked_list.MyLinkedList import MyLinkedList, ListNode


class MyQueue:
    def __init__(self):
        self.items = MyLinkedList()

    # https://www.programiz.com/java-programming/queue
    def add(self, value):
        self.items.add_at_head(value)

    def element(self):
        # get in index must be implemented
        current_node: ListNode = self.items.head
        while current_node:
            if not current_node.next_node:
                break
            else:
                current_node = current_node.next_node

        value = current_node.val
        # delete element from MyLinkedList
        self.items.delete_at_index(self.items.length()-1)
        return value

    def __str__(self):
        return self.items.__str__()