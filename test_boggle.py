import unittest
import boggle
#uppercase charachter [a - z]
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    """
    Out test suits for boggle solver.
    """
    def test_can_create_an_empty_grid(self):
        """
        Test to see whether we can create an empty grid.
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)

    def test_grid_size_is_with_times_height(self):
        """
        Test is not ensured whether the total side of the 
        grid is with*height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid),6)
    
    def grid_coordinates(self):
        """
        Test to ensure that all of the cordinates of the 
        grid can be acessed.
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0,1), grid)
        self.assertIn((1,0), grid)
        self.assertIn((1,1), grid)
        self.assertNotIn((2,2), grid)
    
    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each coordinates of the grid
        contains letters.
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
        