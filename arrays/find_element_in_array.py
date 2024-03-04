def find_element(element, array):
    for i in range(len(array)):
        if array[i] == element:
            print("Element found at index", i)
            return
    print("element not found!")


if __name__ == "__main__":
    import time
    time_start = time.perf_counter()
    numbers = range(10000000)
    find_element(999999999,numbers)
    time_end = time.perf_counter()
    print(time_end - time_start)