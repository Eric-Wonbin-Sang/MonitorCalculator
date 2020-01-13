import pygame

import Functions


class Rect:

    def __init__(self, **kwargs):

        self.kwargs = kwargs

        self.width = kwargs.get("width")
        self.height = kwargs.get("height")
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")
        self.color = self.get_color()

        self.label = kwargs.get("label")

    def get_color(self):
        if self.kwargs.get("color") is None:
            return Functions.get_rand_color()
        return self.kwargs.get("color")

    def reposition(self, x, y):
        self.x = x
        self.y = y

    def draw(self, display, center=False):

        """
        pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        This creates a new object on which you can call the render method.

        textsurface = myfont.render('Some Text', False, (0, 0, 0))
        This creates a new surface with text already drawn onto it. At the end you can just blit the text surface onto your main screen.

        screen.blit(textsurface,(0,0))
        """

        if center:
            center_x, center_y = int(self.x - self.width / 2), int(self.y - self.height / 2)
            pygame.draw.rect(display, self.color, (center_x, center_y, self.width, self.height))
        else:
            pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

        # Functions.draw_font(display, text=str(self.label) + "TEST", x=center_x, y=center_y, color=(255, 255, 255))


def is_colliding(rect_1, rect_2, rect_1_x_delta=0, rect_1_y_delta=0, rect_2_x_delta=0, rect_2_y_delta=0):
    if colliding(rect_1.x + rect_1_x_delta, rect_1.width, rect_1.y + rect_1_y_delta, rect_1.height,
                 rect_2.x + rect_2_x_delta, rect_2.width, rect_2.y + rect_2_y_delta, rect_2.height):
        return True
    return False


def colliding(x1, width1, y1, height1, x2, width2, y2, height2):

    def get_rect_corner_coordinates(x, y, width, height):
        top_left = [x, y]
        top_right = [x + width, y]
        bottom_left = [x, y + height]
        bottom_right = [x + width, y + height]
        return top_left, top_right, bottom_left, bottom_right

    def is_point_in_rect_area(check_x, check_y, x, y, width, height):
        if x <= check_x <= x + width and y <= check_y <= y + height:
            return True
        return False

    coordinates_list_1 = get_rect_corner_coordinates(x1, y1, width1, height1)
    coordinates_list_2 = get_rect_corner_coordinates(x2, y2, width2, height2)

    for coordinates in coordinates_list_1:
        if is_point_in_rect_area(*coordinates, x2, y2, width2, height2):
            return True
    for coordinates in coordinates_list_2:
        if is_point_in_rect_area(*coordinates, x1, y1, width1, height1):
            return True
    return False


def is_point_in_rect(x, y, rect):
    if rect.x <= x <= rect.x + rect.width and rect.y <= y <= rect.y + rect.height:
        return True
    return False
