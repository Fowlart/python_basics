# create array from range
import time
nums = [range(0, 1000000000, 3)]
start_time = time.time()
nums.insert(int(1000000000), 34)
#nums.remove(int(1000000000/2))
end_time = time.time()
print(end_time - start_time)
