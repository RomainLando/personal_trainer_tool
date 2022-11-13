import unittest

from models.goal import Goal

class TestGoal(unittest.TestCase):

    def setUp(self):
        self.goal1 = Goal("General fitness", 8, 9, 3)
        #title, rep_start, rep_end, sets,
        