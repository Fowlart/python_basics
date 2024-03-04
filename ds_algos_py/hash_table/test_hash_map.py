from ds_algos_py.hash_table.MyHashMap import MyHashMap
from ds_algos_py.hash_table.hash_function import get_hash_int

if __name__ == "__main__":
    hash_map = MyHashMap()
    hash_map.put("Artur", "Dev")
    hash_map.put("Olena", "House-keeper")
    hash_map.put("Zenoviy", "Investor")
    print(hash_map.get("Artur"))

    hash_map.delete("Artur")

    # put the value to create collision
    hash_map.put("anelO", "Driver")

    print(hash_map)

    print(hash_map.get("Olena"))
    print(hash_map.get("anelO"))
    print(type(hash_map.get("Olena")))
