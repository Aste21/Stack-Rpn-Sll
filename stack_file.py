class Stack:
    def __init__(self, size, data_type):
        self.size = size
        self.stack = []
        self.data_type = data_type
        self.top_in = -1

    def push(self, element):
        if self.top_in + 2 > self.size:
            print("You've reached maximum stack size!")
        elif self.data_type(element) == element:
            if self.top_in + 1 == len(self.stack):
                self.stack += [self.data_type(element)]
                self.top_in += 1
            else:
                self.top_in += 1
                self.stack[self.top_in] = self.data_type(element)
        else:
            print(f"\n{element}\n")
            print("Incorrect data type")

    def pop(self):
        if self.top_in == -1:
            return None
        else:
            self.top_in -= 1
            return self.stack[self.top_in+1]

    def is_empty(self):
        if self.top_in == -1:
            return True
        return False

    def top(self):
        if self.top_in == -1:
            return None
        else:
            return self.stack[self.top_in]

    def print_stack(self):
        print(self.stack[0:self.top_in+1])


