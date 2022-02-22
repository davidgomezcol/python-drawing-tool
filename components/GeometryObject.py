from abc import ABC, abstractmethod
from . import canvas


class GeometryObject(ABC):
    """Creates a geometry object with pen style
    and geometry type"""
    def __init__(self, geometry_type, pen_style):
        self.canvas = canvas.getInstance()
        self.geometry_type = geometry_type
        self.pen_style = pen_style

    @abstractmethod
    def draw_to_canvas(self):
        pass

    @abstractmethod
    def check_geometry_object_constraints(self):
        pass
