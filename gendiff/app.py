from gendiff.engine import find_diffs
from gendiff.loaders import LOADERS
from gendiff.renders import json_render
import os
import yaml

DEFAULT_FORMAT = {'jsontxt': json_render}
UNKNOWN_FORMAT = 'unknown'
WRONG_OUTPUT_FORMAT_ERROR = "Wrong output format. Try these: " \
                            "'jsontxt', 'json', 'plain'"
WRONG_FILE_FORMAT_ERROR = "Wrong file format. Try these: " \
                          "'.yaml', '.yml', '.json'"


def read_file(path):
    name, ext = os.path.splitext(path)
    loader = LOADERS.get(ext.lower())
    if ext in ('.yml', '.yaml'):
        return yaml.load(open(os.path.realpath(path)), Loader=yaml.BaseLoader)
    if loader is not None:
        return loader(open(os.path.realpath(path)))
    return UNKNOWN_FORMAT


def generate_diff(path1, path2, render=None):
    file1 = read_file(path1)
    file2 = read_file(path2)
    if file1 == UNKNOWN_FORMAT or file2 == UNKNOWN_FORMAT:
        return WRONG_FILE_FORMAT_ERROR
    diff = find_diffs(file1, file2)
    if render is None:
        return DEFAULT_FORMAT['jsontxt'].render(diff)
    return render(diff)
