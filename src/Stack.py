class Stack:
    def __init__(self, data):
        self.stack_data = data

    def add(self, element):
        self.stack_data.append(element)

    def get(self):
        return self.stack_data.pop(-1)


stack = Stack([1, 2, 3])
stack.add(7)


print(stack.get())

