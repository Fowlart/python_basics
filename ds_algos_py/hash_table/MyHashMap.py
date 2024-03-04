from ds_algos_py.my_march_linked_list.MyLinkedList import MyLinkedList


class MyHashMap:
    def __init__(self):
        self.max_array_size: int = 100
        self.internal_array = self.__create_array_of_fixed_size(self.max_array_size)

    def __get_hash_int(self, some) -> int:
        hash_sum = 0
        for char in str(some):
            hash_sum += ord(char)

        return hash_sum % 100

    def __create_array_of_fixed_size(self, n: int) -> list:
        #  return [None for _ in range(n)]
        return [None] * n

    def __put_internal(self, key, value):
        index = self.__get_hash_int(key)
        if len(self.internal_array) <= index:
            # self.internal_array.extend([None] * (index - len(self.internal_array) + 1))
            raise IndexError("Hash Table is full")
        self.internal_array[index] = (key, value)

    def put(self, key, value):
        index = self.__get_hash_int(key)
        key_value_added = (key, value)

        if self.internal_array[index] is not None:

            if isinstance(self.internal_array[index], MyLinkedList):
                existed_list = self.internal_array[index]

                # todo: we need to iterate over LinkedList to see if the tuple with
                #  the key already exists to substitute the value
                for existing in existed_list:
                    if existing[0] == key_value_added[0]:
                        existing = key_value_added
                        return

                existed_list.append(key_value_added)
                return

            key_value_previous: tuple = self.internal_array[index]
            # if keys are the same - just substitute value
            if key_value_previous[0] == key_value_added[0]:
                self.internal_array[index] = key_value_added
                return

            l_list = MyLinkedList()
            l_list.add_at_head(key_value_previous)
            l_list.add_at_head(key_value_added)
            self.internal_array[index] = l_list

        else:
            self.__put_internal(key, value)

    def _get_value_from_linked_list(self, key, linked_list: MyLinkedList):
        head = linked_list.head
        while head is not None:
            if head.val[0] == key:
                return head.val[1]
            head = head.next_node
        return None

    def get(self, key):
        index = self.__get_hash_int(key)
        if index < len(self.internal_array):
            if isinstance(self.internal_array[index], MyLinkedList):
                l_list: MyLinkedList = self.internal_array[index]
                return self._get_value_from_linked_list(key, l_list)
            elif isinstance(self.internal_array[index], tuple):  # check if type is tuple
                return self.internal_array[index][1]  # return value of tuple
            else:
                return None
        else:
            return None

    def delete(self, key):
        index = self.__get_hash_int(key)
        self.internal_array[index] = None

    def __str__(self):
        # filter values from List
        return str([str(n) for n in self.internal_array if n is not None])
