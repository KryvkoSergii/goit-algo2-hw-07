import unittest
from app.tree import SplayTree

class SplayTreeTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        tree = SplayTree()
        tree.insert(1, 10)
        tree.insert(2, 20)
        tree.insert(3, 30)
        tree.insert(4, 40)

        self.tree = tree

    def test_should_find_existing(self):
        self.assertEqual(self.tree.find(2), 20)

    def test_should_not_find_non_existing(self):
        self.assertEqual(self.tree.find(5), None)

    def test_should_insert(self):
        self.tree.insert(50, 500)
        self.assertEqual(self.tree.find(50), 500)

if __name__ == '__main__':
    unittest.main()