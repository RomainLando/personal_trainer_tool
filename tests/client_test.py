import unittest

from models.client import Client
from models.goal import Goal

class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.goal1 = Goal("General fitness", 8, 9, 3)
        self.client1 = Client("Adrien", "Hughes", 42, 170, 85, self.goal1)
    
    def test_client_has_first_name(self):
        self.assertEqual("Adrien", self.client1.first_name)
    
    def test_client_has_last_name(self):
        self.assertEqual("Hughes", self.client1.last_name)
    
    def test_client_has_age(self):
        self.assertEqual(42, self.client1.age)
    
    def test_client_has_height(self):
        self.assertEqual(170, self.client1.height)
    
    def test_cliient_has_weight(self):
        self.assertEqual(85, self.client1.weight)
    
    def test_client_has_goal(self):
        self.assertEqual(3, self.client1.goal.sets)