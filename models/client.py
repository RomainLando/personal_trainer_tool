class Client:
    def __init__(self, first_name, last_name, age, height, weight, goal, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.goal = goal
        self.id = id
    
    def __str__(self):
        return f"Client {self.first_name} {self.last_name}."