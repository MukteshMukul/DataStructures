"""
Sample Implementation of deque class
"""

class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

def main():
    d = Deque()

    print(d.isEmpty())

    d.addFront(2)
    d.addRear(3)
    d.addFront(1)

    print(d.size())
    print(d.items)

    print(d.removeFront())
    print(d.items)

if __name__ == '__main__':
    main()
