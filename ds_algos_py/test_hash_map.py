from ds_algos_py.hash_table.MyHashMap import MyHashMap

if __name__ == "__main__":
    hash_map = MyHashMap()
    hash_map.put("Artur", "Dev")
    hash_map.put("Olena", "House-keeper")
    hash_map.put("Zenoviy", "Investor")
    print(hash_map.get("Artur"))

    hash_map.delete("Artur")

    # put the value to create collision
    hash_map.put("anelO", "Driver")
    hash_map.put("Olena", "Prosecutor")

    print(hash_map.get("Olena"))
    print(hash_map.get("anelO"))
    print(type(hash_map.get("Olena")))

    hash_map.put("Govanni"[::-1], "_")
    hash_map.put("Govanni"[::-1], "Hostile hacker")
    hash_map.put("Govanni", "Soldier of Special Forces")
    hash_map.put("Govanni", "Drone master")
    hash_map.put("Govanni", "Pilot")
    hash_map.put("Govanni", "The liaison officer")

    print(hash_map)

    print(hash_map.get("Govanni"))
    print(hash_map.get("Govanni"[::-1]))
