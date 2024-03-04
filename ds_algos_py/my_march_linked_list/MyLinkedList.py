class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.current_iter_node = None

    # for iteration operator support: should return start of iteration
    def __iter__(self):
        self.current_iter_node = self.head
        return self

    # for iteration operator support: should return next value each time
    def __next__(self):
        if self.current_iter_node:
            val = self.current_iter_node.val
            self.current_iter_node = self.current_iter_node.next_node
            return val
        else:
            raise StopIteration()

    # for implementing membership test to overwrite `in` operator :
    def __contains__(self, value):
        print("called self.__contains__ in MyLinkedList")
        result: bool = False

        for node_value in self:
            if node_value == value:
                result = True
                break

        return result

    def index_of(self, val):
        current = self.head
        index = 0
        while current is not None:
            if current.val == val:
                return index
            current = current.next_node
            index += 1
        return -1

    def append(self, some) -> None:
        if self.head is None:
            self.head = ListNode(val=some)
        else:
            current = self.head

            # go to the tail
            while current.next_node is not None:
                current = current.next_node

            current.next_node = ListNode(val=some)

    def add_at_head(self, val) -> None:
        current = self.head
        self.head = ListNode(val=val)
        self.head.next_node = current

    def add_at_tail(self, val) -> None:
        self.append(val)

    def add_at_index(self, index: int, val) -> None:
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")
        the_range = range(index)
        current: ListNode = self.head
        if index == 0:
            self.add_at_head(val)
        else:
            for i in the_range:
                if current.next_node is None:
                    current.next_node = ListNode(val=val)
                    break
                elif i == the_range[index - 1]:
                    current.next_node = ListNode(val=val, next_node=current.next_node)
                    break
                else:
                    current = current.next_node

    def delete_at_index(self, index: int) -> None:
        the_range = range(index)
        if index == 0:
            self.head = self.head.next_node
        else:
            current = self.head
            for i in the_range:
                if current.next_node is None:
                    raise IndexError("Index out of range")
                elif i == the_range[index - 1]:
                    current.next_node = current.next_node.next_node
                    break
                else:
                    current = current.next_node

    def replace_all_values(self, list_of_values: list) -> None:
        self.head = None
        for val in list_of_values:
            self.add_at_tail(val)

    def length(self) -> int:
        count: int = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def __str__(self) -> str:
        res = []
        current = self.head
        while current is not None:
            res.append(current.val)
            current = current.next_node

        return '|=>'.join(str(i) for i in res)
