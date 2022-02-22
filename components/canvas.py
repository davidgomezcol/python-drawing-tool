class Canvas:
    """Class to create canvas with Width and Height
    which borders are horizontal '-' and vertical '|' """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.x1, self.y1, self.x2, self.y2 = 1, 1, w, h
        self.canvasArray = [[' '] * self.w for i in range(self.h)]
        self.canvasObjects = []

    @staticmethod
    def get_instance():
        return Canvas._instance

    def add_to_canvas(self, geometry_object):
        """Adds the object to the canvas"""
        self.canvasObjects.append(geometry_object)
        return self.canvasObjects

    def print_on_console(self):
        """prints canvas to the console"""
        for obj in self.canvasObjects:
            obj.draw_to_canvas()

        print('-' * (self.w + 2))
        for i in range(self.h):
            row = '|'
            for j in range(self.w):
                row += self.canvasArray[i][j]
            row += '|'
            print(row)
        print('-' * (self.w + 2))

    def erase(self):
        """Erase objects from canvas"""
        self.canvasArray = [[' '] * self.w for i in range(self.h)]
