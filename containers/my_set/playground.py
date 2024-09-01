from ds_algos_py.hash_table.MyHashMap import MyHashMap
from MySet import MySet

if __name__ == "__main__":

    hm = MyHashMap()
    hm.put("one", 1)
    hm.put("two", 2)
    hm.put("zero", 0)
    hm.put("zero", "zero_val")

    print(hm)
    print(hm.get("zero"))

    ms = MySet()
    ms.add_element("one")
    ms.add_element("one")
    ms.add_element("one")
    ms.add_element(1)
    ms.add_element(1)
    ms.add_element(2)
    print(ms)
    print(ms.get_element("two"))

    # is-present
    print(ms.is_present(99))
    print(ms.is_present(1))
    print(ms.is_present("one"))

    print(ms)

    # iterable
    print("\n \nTesting iterable...")
    print(ms)
    for elem in ms:
        print(elem)

    # intersection
    print("\n \nTesting intersection...")
    print(ms.intersection(["one", 2]))
