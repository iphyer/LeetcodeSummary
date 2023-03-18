class BrowserHistory:

    def __init__(self, homepage: str):
        self.history_stack = [homepage]
        self.current = 0        

    def visit(self, url: str) -> None:
        if self.current >= 0:
            self.history_stack = self.history_stack[:self.current+1]
        self.history_stack.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        if steps <= self.current:
            self.current = self.current - steps
        else:
            self.current  = 0      
        return self.history_stack[self.current]
        
    def forward(self, steps: int) -> str:
        if steps <= (len(self.history_stack) - 1 - self.current):
            self.current = self.current + steps
        else:
            self.current  = len(self.history_stack) - 1
        return self.history_stack[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
