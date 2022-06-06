class stack:
    def __init__(self, content: list = None) -> None:
        if content == None:
            self.content = list()
            return
        self.content = content
    
    def is_empty(self):
        return len(self.content) == 0
    
    def push_right(self, element):
        self.content.append(element)

    def pop_right(self):
        return self.content.pop()

    def peek_right(self):
        return self.content[-1]
    
    def __str__(self) -> str:
        return str(self.content)


class deque(stack):

    def push_left(self, element):
        self.content.insert(0, element)
    
    def pop_left(self):
        return self.content.pop(0)
        

    def peek_left(self):
        return self.content[0]