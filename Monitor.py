import math

import Rect
import Functions


class Monitor:

    def __init__(self, **kwargs):

        self.name = kwargs.get("name", "Display")
        self.resolution_height = kwargs.get("resolution_height")
        self.resolution_width = kwargs.get("resolution_width")

        self.width_ratio, self.height_ratio = self.get_width_height_ratio(kwargs)
        self.width, self.height, self.diagonal = self.get_width_height_diagonal(kwargs)

        self.dpi = self.get_dpi()
        self.rect = self.get_rect(kwargs.get("gui_scalar"))     # Monitor class should probably be a child of Rect

    def get_width_height_diagonal(self, kwargs):

        width = kwargs.get("width")
        height = kwargs.get("height")
        diagonal = kwargs.get("diagonal")

        if height is None and width:
            height = (width * self.height_ratio) / self.width_ratio
        if width is None and height:
            width = (height * self.width_ratio) / self.height_ratio
        if diagonal is None and height and width:
            diagonal = math.sqrt(height ** 2 + width ** 2)

        if diagonal:
            multiplier = math.sqrt(diagonal ** 2 / (self.width_ratio ** 2 + self.height_ratio ** 2))
            width = multiplier * self.width_ratio
            height = multiplier * self.height_ratio

        return width, height, diagonal

    def get_width_height_ratio(self, kwargs):
        width_ratio = kwargs.get("width_ratio")
        height_ratio = kwargs.get("height_ratio")

        if width_ratio is None and height_ratio is None and self.resolution_height and self.resolution_width:
            width_ratio = self.resolution_width/gcd(self.resolution_height, self.resolution_width)
            height_ratio = self.resolution_height/gcd(self.resolution_height, self.resolution_width)

        return width_ratio, height_ratio

    def get_dpi(self):
        if self.resolution_width and self.width:
            return self.resolution_width / self.width
        elif self.resolution_height and self.height:
            return self.resolution_height / self.height
        return None

    def get_rect(self, scalar=None):
        if scalar is None:
            scalar = 1
        if self.width and self.height:
            return Rect.Rect(width=self.width * scalar,
                             height=self.height * scalar,
                             x=0, y=0)
        return None

    # Displaying data -----------------------------------------------
    def get_properties_dict(self):
        return {"width": self.width,
                "height": self.height,
                "diagonal": self.diagonal,
                "w to h ratio": [self.width_ratio, self.height_ratio],
                "dpi": self.dpi}

    def to_str(self):
        return Functions.dict_to_str(self.get_properties_dict())


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
