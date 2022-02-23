import unittest
from components.canvas import Canvas
from components.line import Line
from components.block import Block


class TestBlock(unittest.TestCase):
    """Test that a block is created successfully"""

    def setUp(self):
        self.w = 5
        self.h = 4
        self.canvas = Canvas(self.w, self.h)

    def test_draw_to_canvas(self):
        """Test that a block is drawn to the canvas"""
        line = Line(3, 1, 3, 4)
        line.draw_to_canvas()
        block = Block(1, 2, 'o')
        block.draw_to_canvas()
        exp = [
            ['o', 'o', 'x', ' ', ' '],
            ['o', 'o', 'x', ' ', ' '],
            ['o', 'o', 'x', ' ', ' '],
            ['o', 'o', 'x', ' ', ' ']
        ]
        self.assertEqual(exp, self.canvas.canvasArray)

    def test_check_geometry_object_constraints(self):
        """Test geometry constraints of the object"""
        block1 = Block(1, 2)
        block2 = Block(6, 2)
        block3 = Block(1, 6)
        block4 = Block(-1, 2)
        block5 = Block(1, -1)

        self.assertEqual(True, block1.check_geometry_object_constraints())
        self.assertEqual(False, block2.check_geometry_object_constraints())
        self.assertEqual(False, block3.check_geometry_object_constraints())
        self.assertEqual(False, block4.check_geometry_object_constraints())
        self.assertEqual(False, block5.check_geometry_object_constraints())


if __name__ == '__main__':
    unittest.main()
