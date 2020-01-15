import screeninfo
import pygame
import os
import random
import win32api

import Rect


def draw_font(display, text, x, y, size=50, color=(0, 0, 0)):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    display.blit(text, (x, y))


def get_rand_color():
    return random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)


def get_mouse_position(ratio=1.0, x_delta=0, y_delta=0):
    x, y = win32api.GetCursorPos()
    return x * ratio + x_delta, y * ratio + y_delta


def set_mouse_position(x, y):
    win32api.SetCursorPos((int(x), int(y)))


def main():

    monitor_list = screeninfo.get_monitors()

    pygame.init()
    clock = pygame.time.Clock()

    ratio = .2
    x_delta = int(-1 * min([monitor.x * ratio for monitor in monitor_list]))
    y_delta = 0

    display_width = int((max([monitor.x + monitor.width for monitor in monitor_list]) - min([monitor.x for monitor in monitor_list])) * ratio)
    display_height = int((max([monitor.y + monitor.height for monitor in monitor_list]) - min([monitor.y for monitor in monitor_list])) * ratio)

    display = pygame.display.set_mode((display_width, display_height), 0, 32)
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (-10, 0)
    os.environ['SDL_VIDEO_CENTERED'] = '0'

    rect_list = [Rect.Rect(width=monitor.width * ratio, height=monitor.height * ratio,
                           x=monitor.x * ratio + x_delta, y=monitor.y * ratio + y_delta,
                           color=get_rand_color(), label=m_i)
                 for m_i, monitor in enumerate(monitor_list)]
    mouse_rect = Rect.Rect(width=10, height=10, x=0, y=0, color=(255, 255, 255))

    curr_monitor = monitor_list[0]
    prev_monitor = curr_monitor
    while True:

        mouse_position = get_mouse_position(ratio=ratio, x_delta=x_delta, y_delta=y_delta)

        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                quit()

        mouse_rect.reposition(*mouse_position)

        for monitor in monitor_list:
            if monitor.x * ratio + x_delta <= mouse_rect.x <= (monitor.x + monitor.width) * ratio + x_delta:
                curr_monitor = monitor

        if curr_monitor != prev_monitor:
            mouse_rect.y = (curr_monitor.height/prev_monitor.height) * mouse_rect.y
            # Functions.set_mouse_position(mouse_rect.x / ratio + x_delta, mouse_rect.y)

        print(mouse_rect.x, mouse_rect.y)

        display.fill((0, 0, 0))
        for rect in rect_list:
            rect.draw(display)
        mouse_rect.draw(display, center=True)

        pygame.display.flip()
        clock.tick(60)

        prev_monitor = curr_monitor


main()


# import tkinter as tk
# root = tk.Tk()
#
# print(root.children)
#
# width_px = root.winfo_screenwidth()
# height_px = root.winfo_screenheight()
# width_mm = root.winfo_screenmmwidth()
# height_mm = root.winfo_screenmmheight()
# # 2.54 cm = in
# width_in = width_mm / 25.4
# height_in = height_mm / 25.4
# width_dpi = width_px/width_in
# height_dpi = height_px/height_in
#
# print('Width: %i px, Height: %i px' % (width_px, height_px))
# print('Width: %i mm, Height: %i mm' % (width_mm, height_mm))
# print('Width: %f in, Height: %f in' % (width_in, height_in))
# print('Width: %f dpi, Height: %f dpi' % (width_dpi, height_dpi))
#
#
# import ctypes
#
#
# user32 = ctypes.windll.user32
# user32.SetProcessDPIAware()
# [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
# print('Size is %f %f' % (w, h))
#
# curr_dpi = w*96/width_px
# print('Current DPI is %f' % (curr_dpi))


# import subprocess
# import re
#
# proc = subprocess.Popen(['powershell', 'wmic desktopmonitor'], stdout=subprocess.PIPE)
# res = proc.communicate()
#
# # Get-WmiObject -Namespace root\wmi -Class WmiMonitorBasicDisplayParams
# # wmic desktopmonitor
#
# # print(res[0].decode("utf-8"))
# # print(res)
#
# for part in str(res).split("  "):
#     if not part.replace(" ", "") == "":
#         print(part)
#
# # monitors = re.findall('(?s)\r\nName\s+:\s(.*?)\r\n', res[0].decode("utf-8"))
# # print(monitors)
