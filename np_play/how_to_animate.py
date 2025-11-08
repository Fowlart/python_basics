import time
import numpy as np
import sys

def tick():
    clear = "\n" * 1
    print(clear, end="")
    time.sleep(0.5)


def run():
    symbol = 9966

    arr = np.zeros(100).reshape((10, 10))
    i = -1

    while i<=3:
      i+=1
      arr = arr * 0
      match i:
        case 0:
             arr[0] = symbol
             tick()
             print(arr)
        case 1:
             tick()
             arr[:,0]=symbol
             print(arr)
        case 2:
             tick()
             arr[[9]] = symbol
             arr[[0]] = 0
             print(arr)
        case 3:
             tick()
             arr = arr * 0
             arr[:, [9]] = symbol
             print(arr)
             i=-1
        case _:
             print("end")

if __name__ == "__main__":
    log_file_name = ""
    log_file = ""
    if log_file_name and log_file:
        print("Strings not empty!!!")
    print(sys.argv[0])
    run()