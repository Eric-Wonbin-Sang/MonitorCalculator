import pygame
import screeninfo

import Monitor
import Rect
import Functions


def get_pygame_display(monitor_list):
    pixel_width = int(max([monitor.rect.x + monitor.rect.width for monitor in monitor_list])) + 200
    pixel_height = int(max([monitor.rect.y + monitor.rect.height for monitor in monitor_list])) + 200
    return pygame.display.set_mode((pixel_width, pixel_height), 0, 32)


def position_monitors(monitor_list):
    for m_i, monitor in enumerate(monitor_list):
        if m_i == 0:
            monitor.rect.reposition(0, 0)
        else:
            prev_monitor = monitor_list[m_i - 1]
            monitor.rect.reposition(prev_monitor.rect.x + prev_monitor.rect.width,
                                    prev_monitor.rect.y)


def get_monitor_list(gui_scalar):

    # monitor_list = []
    # for monitor in screeninfo.get_monitors():
    #     monitor_list.append(Monitor.Monitor(name=monitor.name,
    #                                         width_ratio=16,
    #                                         height_ratio=9,
    #                                         width=None,
    #                                         height=None,
    #                                         diagonal=None,
    #                                         resolution_width=monitor.width,
    #                                         resolution_height=monitor.height,
    #                                         gui_scalar=gui_scalar))
    #
    #     print(monitor_list[-1].to_str(), "\n------------------------")

    monitor_list = [Monitor.Monitor(name="Left",
                                    width_ratio=16,
                                    height_ratio=9,
                                    width=None,
                                    height=None,
                                    diagonal=23.8,
                                    resolution_width=1920,
                                    resolution_height=1080,
                                    gui_scalar=gui_scalar),
                    Monitor.Monitor(name="Right",
                                    width_ratio=16,
                                    height_ratio=9,
                                    width=None,
                                    height=20.743497783564276,
                                    diagonal=None,
                                    resolution_width=3840,
                                    resolution_height=2160,
                                    gui_scalar=gui_scalar)]

    return monitor_list


def update_curr_monitor_and_remaining_monitor_list(curr_monitor, remaining_monitor_list, monitor_list,
                                                   curr_mouse_dict, prev_mouse_dict):
    for m_i, monitor in enumerate(monitor_list):
        if curr_mouse_dict["left"] and not prev_mouse_dict["left"]:
            if Rect.is_point_in_rect(*curr_mouse_dict["pos"], monitor.rect):
                return monitor, monitor_list[:m_i] + monitor_list[m_i + 1:]
        elif not curr_mouse_dict["left"] and prev_mouse_dict["left"]:
            return None, monitor_list
    return curr_monitor, remaining_monitor_list


def drag_monitor(curr_monitor, remaining_monitor_list, curr_mouse_dict, prev_mouse_dict):
    if curr_monitor is not None and curr_mouse_dict["left"]:

        x_delta, y_delta = [curr_mouse_dict["pos"][i] - prev_mouse_dict["pos"][i] for i in range(2)]

        if not any([Rect.is_colliding(curr_monitor.rect, check_monitor.rect,
                                      rect_1_x_delta=x_delta, rect_1_y_delta=y_delta)
                    for check_monitor in remaining_monitor_list]):
            curr_monitor.rect.reposition(curr_monitor.rect.x + x_delta, curr_monitor.rect.y + y_delta)
        elif not any([Rect.is_colliding(curr_monitor.rect, check_monitor.rect, rect_1_y_delta=y_delta)
                      for check_monitor in remaining_monitor_list]):
            curr_monitor.rect.reposition(curr_monitor.rect.x, curr_monitor.rect.y + y_delta)
        elif not any([Rect.is_colliding(curr_monitor.rect, check_monitor.rect, rect_1_x_delta=x_delta)
                      for check_monitor in remaining_monitor_list]):
            curr_monitor.rect.reposition(curr_monitor.rect.x + x_delta, curr_monitor.rect.y)


def main():

    gui_scalar = 20

    monitor_list = get_monitor_list(gui_scalar)
    position_monitors(monitor_list)

    display = get_pygame_display(monitor_list)
    pygame.init()
    clock = pygame.time.Clock()

    mouse_rect = Rect.Rect(width=10, height=10, x=0, y=0, color=(255, 255, 255))
    pygame_mouse_rect = Rect.Rect(width=10, height=10, x=0, y=0, color=(255, 255, 255))

    prev_mouse_dict = Functions.get_mouse_dict()

    curr_monitor = None
    remaining_monitor_list = monitor_list

    while True:

        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                quit()

        curr_mouse_dict = Functions.get_mouse_dict()

        # mouse_position = Functions.get_mouse_position(gui_scalar=1, x_delta=0, y_delta=0)
        # mouse_rect.reposition(*mouse_position)
        # pygame_mouse_rect.reposition(*curr_mouse_dict["pos"])

        curr_monitor, remaining_monitor_list = update_curr_monitor_and_remaining_monitor_list(
            curr_monitor, remaining_monitor_list, monitor_list, curr_mouse_dict, prev_mouse_dict)
        drag_monitor(curr_monitor, remaining_monitor_list, curr_mouse_dict, prev_mouse_dict)

        # drawing ------------------------------------
        display.fill((0, 0, 40))
        for monitor in monitor_list:
            monitor.rect.draw(display)
        mouse_rect.draw(display, center=True)
        pygame.display.flip()
        clock.tick(60)
        # drawing ------------------------------------

        prev_mouse_dict = curr_mouse_dict


main()
