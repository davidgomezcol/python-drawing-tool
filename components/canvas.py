import os


class Canvas(object):
    """Create canvas with width and height
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

    def print_to_file(self):
        """prints canvas to the console and saves
        output on 'output.txt' file"""
        working_dir = os.getcwd()

        for obj in self.canvasObjects:
            obj.draw_to_canvas()

        try:
            f = open(working_dir + "/files/output.txt", "a")
            f.write('-' * (self.w + 2) + '\n')
            for i in range(self.h):
                row = '|'
                for j in range(self.w):
                    row += self.canvasArray[i][j]
                row += '|'
                f.write(row + '\n')
            f.write('-' * (self.w + 2) + '\n')
            f.close()
            print(
                "Printed on file", "Canvas"
                if len(self.canvasObjects) == 0 else self.canvasObjects[-1]
            )
        except Exception as e:
            print('Error {}'.format(e))

    def erase(self):
        """Erase objects from canvas"""
        self.canvasArray = [[' '] * self.w for i in range(self.h)]

    def __repr__(self):
        return "Canvas"
