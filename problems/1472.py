from collections import deque


class BrowserHistory:

    def __init__(self, homepage: str):
        self.b_hist = deque()
        self.f_hist = deque()
        self.current = (homepage)

    def visit(self, url: str) -> None:
        self.b_hist.append(self.current)
        self.current = url
        self.f_hist = deque()

    def back(self, steps: int) -> str:
        if len(self.b_hist) < steps:
            steps = len(self.b_hist)
        for _ in range(steps):
            self.f_hist.appendleft(self.current)
            self.current = self.b_hist.pop()
        return self.current

    def forward(self, steps: int) -> str:
        if len(self.f_hist) < steps:
            steps = len(self.f_hist)
        for _ in range(steps):
            self.b_hist.append(self.current)
            self.current = self.f_hist.popleft()
        return self.current
