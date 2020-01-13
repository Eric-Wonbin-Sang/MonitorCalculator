import pygame
import screeninfo

import Monitor
import Rect
import Functions


def get_display(pixel_width, pixel_height):
    return pygame.display.set_mode((pixel_width, pixel_height), 0, 32)


def position_monitors(monitor_list):
    for m_i, monitor in enumerate(monitor_list):
        if m_i == 0:
            monitor.rect.reposition(0, 0)
        else:
            prev_monitor = monitor_list[m_i - 1]
            monitor.rect.reposition(prev_monitor.rect.x + prev_monitor.rect.width,
                                    prev_monitor.rect.y)


def main():

    gui_scalar = 20

    monitor_list = screeninfo.get_monitors()
    print(monitor_list)

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
    position_monitors(monitor_list)

    display_width = int(max([monitor.rect.x + monitor.rect.width for monitor in monitor_list])) + 200
    display_height = int(max([monitor.rect.y + monitor.rect.height for monitor in monitor_list])) + 200
    display = get_display(pixel_width=display_width, pixel_height=display_height)
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

        # mouse_position = Functions.get_mouse_position(gui_scalar=1, x_delta=0, y_delta=0)
        # mouse_rect.reposition(*mouse_position)

        curr_mouse_dict = Functions.get_mouse_dict()
        # pygame_mouse_rect.reposition(*curr_mouse_dict["pos"])

        # Getting the currently selected monitor and the list of remaining monitors -----------------------------
        for m_i, monitor in enumerate(monitor_list):
            if curr_mouse_dict["left"] and not prev_mouse_dict["left"]:
                if Rect.is_point_in_rect(*curr_mouse_dict["pos"], monitor.rect):
                    curr_monitor, remaining_monitor_list = monitor, monitor_list[:m_i] + monitor_list[m_i + 1:]
            elif not curr_mouse_dict["left"] and prev_mouse_dict["left"]:
                curr_monitor, remaining_monitor_list = None, monitor_list
        # Getting the currently selected monitor and the list of remaining monitors -----------------------------

        if curr_monitor is not None and curr_mouse_dict["left"]:
            x_delta = curr_mouse_dict["pos"][0] - prev_mouse_dict["pos"][0]
            y_delta = curr_mouse_dict["pos"][1] - prev_mouse_dict["pos"][1]

            truth_list = [Rect.is_colliding(curr_monitor.rect, check_monitor.rect,
                                            rect_1_x_delta=x_delta, rect_1_y_delta=y_delta)
                          for check_monitor in remaining_monitor_list]

            if not any(truth_list):
                curr_monitor.rect.reposition(curr_monitor.rect.x + x_delta, curr_monitor.rect.y + y_delta)
            elif not any([Rect.is_colliding(curr_monitor.rect, check_monitor.rect, rect_1_y_delta=y_delta)
                          for check_monitor in remaining_monitor_list]):
                curr_monitor.rect.reposition(curr_monitor.rect.x, curr_monitor.rect.y + y_delta)
            elif not any([Rect.is_colliding(curr_monitor.rect, check_monitor.rect, rect_1_x_delta=x_delta)
                          for check_monitor in remaining_monitor_list]):
                curr_monitor.rect.reposition(curr_monitor.rect.x + x_delta, curr_monitor.rect.y)

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
