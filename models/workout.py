class Workout:
    def __init__(self, program, exercise, id=None):
        self.program = program
        self.exercise = exercise
        self.id = id

    def __str__(self):
        return f"The exercise {self.exercise.name} is in the program {self.program.title}"