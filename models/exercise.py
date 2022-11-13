class Exercise:
    def __init__(self, name, muscle_group, duration=None, id=None):
        self.name = name
        self.muscle_group = muscle_group
        self.duration = duration
        self.id = id
    
    def __str__(self):
        return f"{self.name}"