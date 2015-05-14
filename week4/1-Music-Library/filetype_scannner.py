import os


def filetype_scan(path, filetype_str):

    if filetype_str[0] != "*":
        filetype_str = filetype_str.replace("*", "")

    if filetype_str[0] != ".":
        filetype_str = "." + filetype_str

    all_files = os.listdir(path)
    files = [x for x in all_files if filetype_str in x]
    return files


def lst_filetype_scan(path, filetype_lst):
    result = {}
    for e in filetype_lst:
        result[e] = filetype_scan(path, str(e))
    return result
