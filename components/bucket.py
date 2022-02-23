from .GeometryObject import GeometryObject


class Bucket(GeometryObject):
    """Creates a geometry object and Bucket fill form"""

    def __init__(self, x, y, pen_style='x'):
        GeometryObject.__init__(self, 'B', pen_style)
        self.x, self.y = x, y

    def draw_to_canvas(self):
        """Bucket Fill to canvas"""
        if self.canvas.x1 <= self.x <= self.canvas.x2 and \
                self.canvas.y1 <= self.y <= self.canvas.y2 and \
                self.canvas.canvasArray[self.y - 1][self.x - 1] == ' ':
            self.canvas.canvasArray[self.y - 1][self.x - 1] = \
                str(self.pen_style)
            bucket_1 = Bucket(self.x, self.y + 1, self.pen_style)
            bucket_2 = Bucket(self.x, self.y - 1, self.pen_style)
            bucket_3 = Bucket(self.x + 1, self.y, self.pen_style)
            bucket_4 = Bucket(self.x - 1, self.y, self.pen_style)

            bucket_1.draw_to_canvas()
            bucket_2.draw_to_canvas()
            bucket_3.draw_to_canvas()
            bucket_4.draw_to_canvas()

    def check_geometry_object_constraints(self):
        """Check geometry constraints. The object should be
        smaller than Canvas"""
        if self.x < min(self.canvas.x1, self.canvas.x2):
            print('X value is smaller than canvas width')
            return False

        if self.x > max(self.canvas.x1, self.canvas.x2):
            print('X value is larger than canvas width')
            return False

        if self.y < min(self.canvas.y1, self.canvas.y2):
            print('Y Value is smaller than canvas height')
            return False

        if self.y > max(self.canvas.y1, self.canvas.y2):
            print('Y Value is larger than canvas height')
            return False

        return True

    def __repr__(self):
        return "Bucket Fill"
