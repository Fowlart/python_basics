import numpy as np

arr = np.arange(25).reshape((5,5))

print(arr)

print()

mask = arr<10

print(mask)

print()

result = np.add(arr,2,where=mask,dtype=np.int64)

# sometimes unexpected results appears
print(result)