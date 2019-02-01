"""
from queue import Queue

tasks_que = Queue()

i = 0;
while True:
        if not tasks_que.full():
            tasks_que.put(i)
        i+=1

while True:
        if not tasks_que.empty():
            print(task.que.pop())
            tasks_que.task_done()

The program above will never reach the second while loop.
Modify the program so it uses threadding and thereby do all its tasks.
"""



import threading
from queue import Queue

q = Queue()

class listener(object):
    def __init__(self):
        thread = threading.Thread(target=self.loop)
        # thread.daemon = True
        thread.start()

    def loop(self):
        for i in range(0,13):
            q.put(i)

class ui(object):
    def __init__(self):
        listener()
        while True:
            item = q.get()
            print(item)
            if item == 10:
                break
ui()