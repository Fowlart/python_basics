from typing import Iterable

from ds_algos_py.hash_table.MyHashMap import MyHashMap


class MySet:
    def intersection(self, the_iter: Iterable):
        intersection = set()
        for el in the_iter:
            if self.is_present(el):
                intersection.add(el)
        return intersection

    # iteration
    def __internal_array_without_nulls__(self):
        return [el[0] for el in self.internal_hash_map.internal_array if el is not None]

    def __iter__(self):
        return self.__internal_array_without_nulls__().__iter__()

    def __next__(self):
        return self.__internal_array_without_nulls__().__iter__().__next__()

    def __init__(self):
        self.internal_hash_map = MyHashMap()

    def add_element(self, element):
        self.internal_hash_map.put(element, element)

    def get_element(self, element):
        return self.internal_hash_map.get(element)

    def is_present(self, element) -> bool:
        return None != (self.internal_hash_map.get(element))

    def __str__(self):
        int_arr = self.internal_hash_map.internal_array

        return "|".join({str(x[0]) for x in int_arr if x is not None})
