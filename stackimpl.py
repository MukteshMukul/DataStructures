"""
Implementation of stack class
"""

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)




def main():
    s = Stack()
    print(s.isEmpty())

    s.push(1)
    print(s.isEmpty())
    print(s.items)

    s.push(2)
    s.push(3)

    print(s.peek())

    print(s.items)
    print(s.pop())
    print(s.items)




if __name__ == '__main__':
    main()
