def get_hash_int(some) -> int:
    hash_sum = 0
    for char in str(some):
        hash_sum += ord(char)

    return hash_sum % 100


def create_array_of_fixed_size(n: int) -> list:
    #  return [None for _ in range(n)]
    return [None] * n


def get_dictionary() -> dict[int, str]:
    return {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}


if __name__ == '__main__':
    some_str: str = "hello Olenka!"
    reversed_str: str = some_str[::-1]
    print(f"{some_str} <-> {reversed_str}")

    print(get_hash_int(some_str))
    print(get_hash_int(reversed_str))

    print(get_dictionary())
    print(get_dictionary()[3])

    print(create_array_of_fixed_size(10))
