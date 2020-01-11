import math


def get_dimensions(width_ratio=None,
                   height_ratio=None,
                   width=None, height=None,
                   diagonal=None,
                   resolution_height=None,
                   resolution_width=None):

    if height is None and width:
        height = (width * height_ratio) / width_ratio
    if width is None and height:
        width = (height * width_ratio) / height_ratio
    if diagonal is None:
        diagonal = math.sqrt(height**2 + width**2)

    multiplier = math.sqrt(diagonal ** 2 / (width_ratio ** 2 + height_ratio ** 2))
    width = multiplier * width_ratio
    height = multiplier * height_ratio

    dpi = None
    if resolution_width:
        dpi = resolution_width / width
    elif resolution_height:
        dpi = resolution_height / height

    ret_dict = {"width": width,
                "height": height,
                "diagonal": diagonal,
                "w to h ratio": [width_ratio, height_ratio],
                "dpi": dpi}

    return ret_dict


def print_dict(data_dict):

    ret_str = ""
    for i, key in enumerate(data_dict):
        if i != 0:
            ret_str += "\n"
        ret_str += "{}: \t{}".format(key, data_dict[key])
    print(ret_str)


def main():
    print_dict(get_dimensions(width_ratio=16,
                              height_ratio=9,
                              width=None,
                              height=None,
                              diagonal=23.8,
                              resolution_width=1920,
                              resolution_height=1080))

    print("------------------------------")

    print_dict(get_dimensions(width_ratio=16,
                              height_ratio=9,
                              width=None,
                              height=20.743497783564276,
                              diagonal=None,
                              resolution_width=3840,
                              resolution_height=2160))


main()
