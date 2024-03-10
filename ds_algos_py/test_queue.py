from ds_algos_py.queue.MyQueue import MyQueue

import time as t
import datetime as dt

if __name__ == '__main__':
    q = MyQueue()
    for i in range(10):
        q.add(dt.datetime.now())
        t.sleep(1)

    print(q.element())
    print(q.element())
    print(q.element())


