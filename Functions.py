
def dict_to_str(data_dict):
    ret_str = ""
    for i, key in enumerate(data_dict):
        if i != 0:
            ret_str += "\n"
        ret_str += "{}: \t{}".format(key, data_dict[key])
    return ret_str
