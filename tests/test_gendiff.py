from gendiff.engine import find_diff
from gendiff.app import render_diffs, read_file,\
    WRONG_FILE_FORMAT_ERROR, WRONG_OUTPUT_FORMAT_ERROR
from gendiff.renders import json_render
from tests import test_data
import pytest
import os


def get_file_content(path):
    f = open(path, 'r')
    return f.read()


JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
JSONTXT_RES = 'tests/fixtures/json_txt_res'
YAML1 = 'tests/fixtures/yaml1.yml'
YAML2 = 'tests/fixtures/yaml2.yaml'
YAML_RES = 'tests/fixtures/yaml_res'
EXP_JSON_RES = get_file_content(JSONTXT_RES)
EXP_YAML_RES = get_file_content(YAML_RES)


class TestJSON:
    @pytest.mark.parametrize('data1,data2,exp_res',
                             [(test_data.first_file1,
                              test_data.second_file1,
                              test_data.raw_diff1),
                              (test_data.first_file2,
                               test_data.second_file2,
                               test_data.raw_diff2)])
    def test_find_diff(self, data1, data2, exp_res):
        diff = find_diff(data1, data2)
        assert diff == exp_res

    def test_render_diffs(self):
        exp_res = get_file_content(JSONTXT_RES)
        assert json_render.render(test_data.raw_diff1) == exp_res


class TestYaml:
    def test_yml_and_yaml(self):
        exp_res = get_file_content(YAML_RES)
        assert render_diffs(json_render.render, YAML1, YAML2) == EXP_YAML_RES


class TestPaths:
    def test_relpath(self):
        assert render_diffs(json_render.render,
                            JSON1, JSON2) == EXP_JSON_RES

    def test_abspath(self):
        assert render_diffs(json_render.render,
                            os.path.abspath(JSON1), JSON2) == EXP_JSON_RES

    def test_abspath(self):
        assert render_diffs(json_render.render,
                            os.path.abspath(JSON1),
                            os.path.abspath(JSON2)) == EXP_JSON_RES

    def test_wrong_format(self):
        assert render_diffs(json_render.render, JSON1, 'test.txt')\
            == WRONG_FILE_FORMAT_ERROR


class TestFormat:
    def test_wrong_format(self):
        assert render_diffs(None, JSON1, JSON2) == WRONG_OUTPUT_FORMAT_ERROR
