# test_farmquill.py
"""
Tests for FarmQuill module.
"""

import unittest
from farmquill import FarmQuill

class TestFarmQuill(unittest.TestCase):
    """Test cases for FarmQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FarmQuill()
        self.assertIsInstance(instance, FarmQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FarmQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
