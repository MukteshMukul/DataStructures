"""
Queue Implementation
"""

class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    mq = Queue()

    mq.enqueue(2)
    mq.enqueue(3)
    mq.enqueue(4)

    print(mq.items)

    print(mq.dequeue())

    print(mq.size())

    print(mq.isEmpty())
