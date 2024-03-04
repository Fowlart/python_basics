import time

if __name__ == '__main__':
    number = range(20000)

# find duplicates
    time_start = time.perf_counter()
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if number[i] == number[j]:
                print(f"The {number[i]} is duplicate")
    time_end = time.perf_counter()
    time_elapsed = time_end - time_start
    print(f"The time elapsed is {time_elapsed}")
