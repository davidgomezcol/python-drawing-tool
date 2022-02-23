import unittest
from components.canvas import Canvas
from components.line import Line


class TestCanvas(unittest.TestCase):
    """Test for the canvas creation, addition
    and erase"""

    def setUp(self):
        self.w = 4
        self.h = 3
        self.canvas = Canvas(self.w, self.h)
        self.testCanvasArray = [[' '] * self.w for i in range(self.h)]

    def test_create_canvas(self):
        """Test canvas creation"""
        self.assertEqual(self.w, self.canvas.w)
        self.assertEqual(self.h, self.canvas.h)
        self.assertEqual(self.testCanvasArray, self.canvas.canvasArray)
        self.assertEqual([], self.canvas.canvasObjects)

    def test_erase(self):
        """Test erase canvas"""
        x1, y1, x2, y2 = 1, 1, 3, 1
        line = Line(x1, y1, x2, y2)
        line.draw_to_canvas()
        exp = [
            ['x', 'x', 'x', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]
        self.assertEqual(exp, self.canvas.canvasArray)
        self.canvas.erase()
        self.assertEqual(self.testCanvasArray, self.canvas.canvasArray)

    def test_add_to_canvas(self):
        """"Test add to canvas"""
        x1, y1, x2, y2 = 1, 1, 3, 1
        line = Line(x1, y1, x2, y2, pen_style='x')
        self.assertEqual(0, len(self.canvas.canvasObjects))
        self.canvas.add_to_canvas(line)
        self.assertEqual(1, len(self.canvas.canvasObjects))


if __name__ == '__main__':
    unittest.main()
