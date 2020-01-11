import Monitor


def main():
    monitor_0 = Monitor.Monitor(width_ratio=16,
                                height_ratio=9,
                                width=None,
                                height=None,
                                diagonal=23.8,
                                resolution_width=1920,
                                resolution_height=1080)

    monitor_1 = Monitor.Monitor(width_ratio=16,
                                height_ratio=9,
                                width=None,
                                height=20.743497783564276,
                                diagonal=None,
                                resolution_width=3840,
                                resolution_height=2160)

    print(monitor_0.to_str())
    print(monitor_1.to_str())


main()
