import random
import pygame
import win32api


def dict_to_str(data_dict):
    ret_str = ""
    for i, key in enumerate(data_dict):
        if i != 0:
            ret_str += "\n"
        ret_str += "{}: \t{}".format(key, data_dict[key])
    return ret_str


def get_rand_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_mouse_position(gui_scalar=1.0, x_delta=0, y_delta=0):
    x, y = win32api.GetCursorPos()
    return x * gui_scalar + x_delta, y * gui_scalar + y_delta


def get_mouse_dict():
    pressed_button_list = pygame.mouse.get_pressed()
    return {"pos": pygame.mouse.get_pos(),
            "left": pressed_button_list[0],
            "middle": pressed_button_list[1],
            "right": pressed_button_list[2]}
