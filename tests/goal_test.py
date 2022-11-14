import unittest

from models.goal import Goal

class TestGoal(unittest.TestCase):

    def setUp(self):
        self.goal1 = Goal("General fitness", 8, 9, 3)
        self.goal2 = Goal("Hypertrophy", 6, 12, 4)
        
    def test_goal_has_title(self):
        self.assertEqual("General fitness", self.goal1.title)

    def test_goal_has_start_range(self):
        self.assertEqual(6, self.goal2.rep_start)

    def test_goal_has_end_range(self):
        self.assertEqual(12, self.goal2.rep_end)
    
    def test_goal_has_set(self):
        self.assertEqual(3, self.goal1.sets)
    
    def test_goal_id_is_none(self):
        self.assertIsNone(self.goal2.id)
    