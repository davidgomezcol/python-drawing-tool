import unittest
from components.canvas import Canvas
from components.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the rectangle creation"""

    def setUp(self):
        self.w = 5
        self.h = 4
        self.canvas = Canvas(self.w, self.h)

    def test_draw_to_canvas(self):
        """Test to draw a rectangle on canvas"""
        x1, y1, x2, y2 = 1, 1, 3, 3
        rectangle = Rectangle(x1, y1, x2, y2)
        rectangle.draw_to_canvas()

        exp = [
            ['x', 'x', 'x', ' ', ' '],
            ['x', ' ', 'x', ' ', ' '],
            ['x', 'x', 'x', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
        self.assertEqual(exp, self.canvas.canvasArray)

    def test_check_geometry_object_constraints(self):
        """Test to check the geometry constraints of the
        object"""
        x11, y11, x21, y21 = 1, 1, 3, 3
        x12, y12, x22, y22 = 1, 1, 6, 3
        x13, y13, x23, y23 = -1, 1, 3, 3
        x14, y14, x24, y24 = 1, 1, 3, 5
        x15, y15, x25, y25 = 1, -1, 3, 3
        x16, y16, x26, y26 = 3, 3, 1, 1

        rectangle1 = Rectangle(x11, y11, x21, y21)
        rectangle2 = Rectangle(x12, y12, x22, y22)
        rectangle3 = Rectangle(x13, y13, x23, y23)
        rectangle4 = Rectangle(x14, y14, x24, y24)
        rectangle5 = Rectangle(x15, y15, x25, y25)
        rectangle6 = Rectangle(x16, y16, x26, y26)

        self.assertTrue(rectangle1.check_geometry_object_constraints())
        self.assertFalse(rectangle2.check_geometry_object_constraints())
        self.assertFalse(rectangle3.check_geometry_object_constraints())
        self.assertFalse(rectangle4.check_geometry_object_constraints())
        self.assertFalse(rectangle5.check_geometry_object_constraints())
        self.assertFalse(rectangle6.check_geometry_object_constraints())


if __name__ == '__main__':
    unittest.main()
