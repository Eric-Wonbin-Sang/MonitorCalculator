import math

import Rect
import Functions


class Monitor:

    def __init__(self, **kwargs):

        self.name = kwargs.get("name", "Display")
        self.width_ratio = kwargs.get("width_ratio")
        self.height_ratio = kwargs.get("height_ratio")

        self.width, self.height, self.diagonal = self.get_width_height_diagonal(kwargs)

        self.resolution_height = kwargs.get("resolution_height")
        self.resolution_width = kwargs.get("resolution_width")

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
        if diagonal is None:
            diagonal = math.sqrt(height ** 2 + width ** 2)

        multiplier = math.sqrt(diagonal ** 2 / (self.width_ratio ** 2 + self.height_ratio ** 2))
        width = multiplier * self.width_ratio
        height = multiplier * self.height_ratio

        return width, height, diagonal

    def get_dpi(self):
        if self.resolution_width:
            return self.resolution_width / self.width
        elif self.resolution_height:
            return self.resolution_height / self.height
        return None

    def get_rect(self, scalar=None):
        if scalar is None:
            scalar = 1
        return Rect.Rect(width=self.width * scalar,
                         height=self.height * scalar,
                         x=0, y=0)

    # Displaying data -----------------------------------------------
    def get_properties_dict(self):
        return {"width": self.width,
                "height": self.height,
                "diagonal": self.diagonal,
                "w to h ratio": [self.width_ratio, self.height_ratio],
                "dpi": self.dpi}

    def to_str(self):
        return Functions.dict_to_str(self.get_properties_dict())
