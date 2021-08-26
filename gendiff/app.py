from gendiff.engine import generate_diff
from gendiff import LOADERS
import os


UNKNOWN_FORMAT = 'unknown'
WRONG_OUTPUT_FORMAT_ERROR = "Wrong output format. Try these: " \
                              "'jsontxt', 'json', 'plain'"
WRONG_FILE_FORMAT_ERROR = "Wrong file format. Try these: " \
                            "'.yaml', '.yml', '.json'"


def read_file(path):
    name, ext = os.path.splitext(path)
    loader = LOADERS.get(ext.lower())
    if loader is not None:
        return loader(open(os.path.realpath(path)))
    return UNKNOWN_FORMAT


def render_diffs(render, path1, path2):
    if render is None:
        return WRONG_OUTPUT_FORMAT_ERROR
    file1 = read_file(path1)
    file2 = read_file(path2)
    if file1 == UNKNOWN_FORMAT or file2 == UNKNOWN_FORMAT:
        return WRONG_FILE_FORMAT_ERROR
    diff = generate_diff(file1, file2)
    return render(diff)
