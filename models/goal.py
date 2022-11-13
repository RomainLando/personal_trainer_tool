class Goal:
    def __init__(self, title, rep_start, rep_end, sets, id=None):
        self.title = title
        self.rep_start = rep_start
        self.rep_end = rep_end
        self.sets = sets
        self.id = id
    
    def __str__(self):
        return f"Goal: {self.title}"