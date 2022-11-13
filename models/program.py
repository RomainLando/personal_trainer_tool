class Program:
    def __init__(self, title, id=None):
        self.title = title
        self.id = id

    def __str__(self):
        return f"Program: {self.title}"