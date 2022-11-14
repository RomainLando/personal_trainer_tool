import unittest

from models.client_program import ClientProgram
from models.client import Client
from models.program import Program
from models.goal import Goal


class TestClientProgram(unittest.TestCase):

    def setUp(self):
        self.program1 = Program("Legs")
        self.goal1 = Goal("General fitness", 8, 9, 3)
        self.client1 = Client("Adrien", "Hughes", 42, 170, 85, self.goal1)
        self.client_program1 = ClientProgram(self.client1, self.program1)

    def test_client_program_has_client(self):
        self.assertEqual("Adrien", self.client_program1.client.first_name)
    
    def test_client_program_has_program(self):
        self.assertEqual("Legs", self.client_program1.program.title)

    def test_client_program_id_is_none(self):
        self.assertIsNone(self.client_program1.id)