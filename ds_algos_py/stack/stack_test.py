a_list = ["=1=", "=2=", "=3=", "=4="]
print(a_list.pop())
print(a_list.pop())
print(a_list)

from collections import deque

my_stack = deque()
my_stack.append("=1=")
my_stack.append("=2=")
my_stack.append("=3=")
my_stack.append("=4=")
print(my_stack.pop())
print(my_stack.popleft())

# command to list all of methods
dir(my_stack)

print(type(my_stack))
