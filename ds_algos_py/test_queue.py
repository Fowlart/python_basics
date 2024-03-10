from ds_algos_py.queue.MyQueue import MyQueue

if __name__ == '__main__':
    my_queue = MyQueue()
    my_queue.add("one")
    my_queue.add("two")
    my_queue.add("three")
    print(my_queue)
    my_queue.element()
    print(my_queue)
    my_queue.element()
    print(my_queue)
    my_queue.element()
    print(my_queue)
