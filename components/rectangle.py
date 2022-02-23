from .GeometryObject import GeometryObject
from .line import Line


class Rectangle(GeometryObject):
    """Creates a rectangle object"""

    def __init__(self, x1, y1, x2, y2, pen_style='x'):
        GeometryObject.__init__(self, 'R', pen_style)
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2

    def draw_to_canvas(self):
        """Draws lines to canvas"""
        line1 = Line(self.x1, self.y1, self.x2, self.y1)
        line2 = Line(self.x1, self.y2, self.x2, self.y2)
        line3 = Line(self.x1, self.y1, self.x1, self.y2)
        line4 = Line(self.x2, self.y1, self.x2, self.y2)

        line1.draw_to_canvas()
        line2.draw_to_canvas()
        line3.draw_to_canvas()
        line4.draw_to_canvas()

    def check_geometry_object_constraints(self):
        """Check geometry constraints. The object should be
        smaller than Canvas"""
        if self.x1 > self.x2 or self.y1 > self.y2:
            print('Wrong values for X or Y. Please verify.')
            return False

        if min(self.x1, self.x2) < min(self.canvas.x1, self.canvas.x2):
            print('X value is smaller than width canvas')
            return False

        if max(self.x1, self.x2) > max(self.canvas.x1, self.canvas.x2):
            print('X value is larger than width canvas')
            return False

        if min(self.y1, self.y2) < min(self.canvas.y1, self.canvas.y2):
            print('Y value is smaller than height canvas')
            return False

        if max(self.y1, self.y2) > max(self.canvas.y1, self.canvas.y2):
            print('Y value is larger than height canvas')
            return False

        return True

    def __repr__(self):
        return "Rectangle"
