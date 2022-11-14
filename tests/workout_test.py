import unittest

from models.workout import Workout
from models.program import Program
from models.exercise import Exercise

class TestWorkout(unittest.TestCase):

    def setUp(self):
        self.exercise1 = Exercise("Squats", "Legs")
        self.program1 = Program("Legs")
        self.workout1 = Workout(self.program1, self.exercise1)

    def test_workout_has_exercise(self):
        self.assertEqual("Squats", self.workout1.exercise.name)
    
    def test_workout_has_program(self):
        self.assertEqual("Legs", self.workout1.program.title)
    
    def test_workout_id_is_none(self):
        self.assertIsNone(self.workout1.id)
