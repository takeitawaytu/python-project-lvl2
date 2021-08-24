from gendiff.scripts.gendiff import find_diff, render_diffs, \
    read_file
from gendiff.renders import json_render
from tests import test_data
import pytest

JSON1 = 'tests/fixtures/json1.json'
JSON2 = 'tests/fixtures/json2.json'
JSONTXT_RES = 'tests/fixtures/json_txt_res'


def get_file_content(path):
    f = open(path, 'r')
    return f.read()

@pytest.mark.parametrize('data1,data2,exp_res',
                         [(test_data.first_file,
                          test_data.second_file,
                          test_data.raw_diff)])
def test_find_diff(data1, data2, exp_res):
    diff = find_diff(data1, data2)
    assert diff == exp_res


def test_render_diffs():
    exp_res = get_file_content(JSONTXT_RES)
    assert json_render.render(test_data.raw_diff) == exp_res
