import unittest

from models.program import Program

class TestProgram(unittest.TestCase):

    def setUp(self):
        self.program1 = Program("Legs")
    
    def test_program_has_title(self):
        self.assertEqual("Legs", self.program1.title)
    
    def test_program_id_is_none(self):
        self.assertIsNone(self.program1.id)
