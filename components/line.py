from . import GeometryObject


class Line(GeometryObject):
    def __init__(self, x1, x2, y1, y2, pen_style='x'):
        GeometryObject.__init__(self, 'L', pen_style)
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2

    def draw_to_canvas(self):
        for i in range(self.canvas.h):
            for j in range(self.canvas.w):
                if i in range(min([self.y1, self.y2]) - 1, max([self.y1, self.y2])) and \
                        j in range(min([self.x1, self.x2]) - 1, max(self.x1, self.x2)):
                    self.canvas.canvasArray[i][j] = self.pen_style

    def check_geometry_object_constraints(self):
        if (self.x1 < 0) or (self.x2 < 0) or (self.y1 < 0) or (self.y2 < 0):
            print('X and Y values need to be larger than zero (0)')
            return False

        elif min(self.x1, self.x2) < min(self.canvas.x1, self.canvas.x2):
            print('X value is smaller than canvas width')
            return False

        elif max(self.x1, self.x2) > max(self.canvas.x1, self.canvas.x2):
            print("X value is larger than canvas width")
            return False

        elif min(self.y1, self.y2) > max(self.canvas.y1, self.canvas.y2):
            print("Y value is larger that canvas height")
            return False

        elif (self.x1 != self.x2) and (self.y1 != self.y2):
            print("Only horizontal or vertical lines can be drawn")
            return False

        return True
