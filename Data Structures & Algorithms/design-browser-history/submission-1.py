class BrowserHistory:
    class Node:
        def __init__(self, url: str):
            self.next = None
            self.prev = None
            self.url = url
    def __init__(self, homepage: str):
        self.head = self.Node(homepage)

    def visit(self, url: str) -> None:
        new_node = self.Node(url)
        self.head.next = new_node
        new_node.prev = self.head
        self.head = new_node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.head.prev is not None:
                self.head = self.head.prev
        return self.head.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.head.next is not None:
                self.head = self.head.next
        return self.head.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)