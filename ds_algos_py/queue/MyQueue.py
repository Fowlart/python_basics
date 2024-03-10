from ds_algos_py.my_march_linked_list.MyLinkedList import MyLinkedList


class MyQueue:
    def __init__(self):
        self.items = MyLinkedList()

    # https://www.programiz.com/java-programming/queue
    def add(self, value):
        self.items.add_at_head(value)

    def element(self):
        # get in index must be implemented
        return self.items

