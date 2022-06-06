class stack:
    def __init__(self, content: list = None) -> None:
        if content == None:
            self.content = list()
            return
        self.content = content
    
    def is_empty(self):
        return len(self.content) == 0
    
    def pushright(self, element):
        self.content.append(element)

    def popright(self):
        return self.content.pop()

    def peekright(self):
        return self.content[-1]
    
    def __str__(self) -> str:
        return str(self.content)


class deque(stack):

    def pushleft(self, element):
        self.content.insert(0, element)
    
    def popleft(self):
        return self.content.pop(0)
        

    def peekleft(self):
        return self.content[0]