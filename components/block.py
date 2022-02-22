from . import GeometryObject


class Block(GeometryObject):
    """Creates a geometry object and Block form"""
    def __init__(self, x, y, pen_style='x'):
        GeometryObject.__init__(self, 'B', pen_style)
        self.x, self.y = x, y

    def draw_to_canvas(self):
        """Draws block to canvas"""
        if self.canvas.x1 <= self.x <= self.canvas.x2 and \
                self.canvas.y1 <= self.y <= self.canvas.y2 and \
                self.canvas.canvasArray[self.y - 1][self.x - 1] == ' ':
            block_1 = Block(self.x, self.y + 1, self.pen_style)
            block_1.draw_to_canvas()
            block_2 = Block(self.x, self.y - 1, self.pen_style)
            block_2.draw_to_canvas()
            block_3 = Block(self.x + 1, self.y, self.pen_style)
            block_3.draw_to_canvas()
            block_4 = Block(self.x - 1, self.y, self.pen_style)
            block_4.draw_to_canvas()

    def check_geometry_object_constraints(self):
        """Check geometry constraints. The object should be
        smaller than Canvas"""
        if self.x < min(self.canvas.x1, self.canvas.x2):
            print('X value is smaller than width canvas')
            return False

        elif self.x > max(self.canvas.x1, self.canvas.x2):
            print('X value is larger that width canvas')
            return False

        elif self.y < min(self.canvas.y1, self.canvas.y2):
            print('Y Value is smaller that height canvas')
            return False

        elif self.y > max(self.canvas.y1, self.canvas.y2):
            print('Y Value is larger than height canvas')
            return False

        return True
