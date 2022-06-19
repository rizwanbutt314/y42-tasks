

class Stack:

    def __init__(self):
        self.elements = []

    def size(self) -> int:
        return len(self.elements)

    def push(self, element):
        if not element:
            raise Exception("Invalid element")
        self.elements.append(element)

    def pop(self):
        if self.empty():
            raise Exception("Empty stack")

        poped_element = self.elements.pop()
        return poped_element

    def peek(self):
        if self.empty():
            raise Exception("Empty stack")
        return self.elements[-1]

    def empty(self) -> bool:
        return len(self.elements) < 1
