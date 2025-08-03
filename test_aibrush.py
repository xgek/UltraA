# test_aibrush.py
"""
Tests for AIBrush module.
"""

import unittest
from aibrush import AIBrush

class TestAIBrush(unittest.TestCase):
    """Test cases for AIBrush class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AIBrush()
        self.assertIsInstance(instance, AIBrush)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AIBrush()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
