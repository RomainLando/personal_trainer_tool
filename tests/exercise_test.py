import unittest

from models.exercise import Exercise

class TestExercise(unittest.TestCase):

    def setUp(self):
        self.exercise1 = Exercise("Squats", "Legs")
        self.exercise2 = Exercise("Jogging", "Full Body", 30)
    
    def test_exercise_has_name(self):
        self.assertEqual("Squats", self.exercise1.name)
    
    def test_exercise_has_muscle_group(self):
        self.assertEqual("Full Body", self.exercise2.muscle_group)
    
    def test_exercise_has_duration(self):
        self.assertEqual(30, self.exercise2.duration)
    
    def test_exercise_id_is_none(self):
        self.assertIsNone(self.exercise2.id)
    
    def test_exercise_duration_is_none(self):
        self.assertIsNone(self.exercise1.duration)