import unittest
from components.canvas import Canvas
from components.line import Line
from components.bucket import Bucket


class TestBucket(unittest.TestCase):
    """Test that a bucket is created successfully"""

    def setUp(self):
        self.w = 5
        self.h = 4
        self.canvas = Canvas(self.w, self.h)

    def test_draw_to_canvas(self):
        """Test that a Bucket is drawn to the canvas"""
        line = Line(3, 1, 3, 4)
        line.draw_to_canvas()
        bucket = Bucket(1, 2, 'o')
        bucket.draw_to_canvas()
        exp = [
            ['o', 'o', 'x', ' ', ' '],
            ['o', 'o', 'x', ' ', ' '],
            ['o', 'o', 'x', ' ', ' '],
            ['o', 'o', 'x', ' ', ' ']
        ]
        self.assertEqual(exp, self.canvas.canvasArray)

    def test_check_geometry_object_constraints(self):
        """Test geometry constraints of the object"""
        bucket_1 = Bucket(1, 2)
        bucket_2 = Bucket(6, 2)
        bucket_3 = Bucket(1, 6)
        bucket_4 = Bucket(-1, 2)
        bucket_5 = Bucket(1, -1)

        self.assertTrue(bucket_1.check_geometry_object_constraints())
        self.assertFalse(bucket_2.check_geometry_object_constraints())
        self.assertFalse(bucket_3.check_geometry_object_constraints())
        self.assertFalse(bucket_4.check_geometry_object_constraints())
        self.assertFalse(bucket_5.check_geometry_object_constraints())


if __name__ == '__main__':
    unittest.main()
