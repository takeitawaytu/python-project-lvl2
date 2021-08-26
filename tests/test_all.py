from gendiff.engine import find_diffs
from gendiff.app import generate_diff, read_file,\
    WRONG_FILE_FORMAT_ERROR, WRONG_OUTPUT_FORMAT_ERROR
from gendiff.renders import json_render, plain
from tests import test_data
import pytest
import os


def get_file_content(path):
    f = open(path, 'r')
    return f.read()


JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
JSONTXT_RES = 'tests/fixtures/json_txt_res'
JSON1_TREE = 'tests/fixtures/file1_tree.json'
JSON2_TREE = 'tests/fixtures/file2_tree.json'
JSONTXT_RES_TREE = 'tests/fixtures/json_res_tree'
YAML1 = 'tests/fixtures/yaml1.yml'
YAML2 = 'tests/fixtures/yaml2.yaml'
YAML_RES = 'tests/fixtures/yaml_res'
YAML1_TREE = 'tests/fixtures/file1_tree.yaml'
YAML2_TREE = 'tests/fixtures/file2_tree.yaml'
YAML_RES_TREE = 'tests/fixtures/yaml_res_tree'
PLAIN_RES = 'tests/fixtures/plain_res'
EXP_JSON_RES = get_file_content(JSONTXT_RES)
EXP_YAML_RES = get_file_content(YAML_RES)
EXP_JSON_RES_TREE = get_file_content(JSONTXT_RES_TREE)
EXP_YAML_RES_TREE = get_file_content(YAML_RES_TREE)
EXP_PLAIN = get_file_content(PLAIN_RES)


class TestJSON:
    @pytest.mark.parametrize('data1,data2,exp_res',
                             [(test_data.first_file1,
                              test_data.second_file1,
                              test_data.raw_diff1),
                              (test_data.first_file2,
                               test_data.second_file2,
                               test_data.raw_diff2)])
    def test_find_diff(self, data1, data2, exp_res):
        diff = find_diffs(data1, data2)
        assert diff == exp_res

    def test_render_diffs(self):
        assert json_render.render(test_data.raw_diff1) == EXP_JSON_RES

    def test_render_diffs_tree(self):
        assert generate_diff(json_render.render, JSON1_TREE, JSON2_TREE) == EXP_JSON_RES_TREE


class TestYaml:
    def test_yml_and_yaml(self):
        assert generate_diff(json_render.render, YAML1, YAML2) == EXP_YAML_RES

    def test_yml_and_yaml_tree(self):
        assert generate_diff(json_render.render, YAML1_TREE, YAML2_TREE) == EXP_YAML_RES_TREE


class TestPlain:
    def test_plain_json(self):
        assert generate_diff(plain.render, JSON1_TREE, JSON2_TREE) == EXP_PLAIN

    def test_plain_json(self):
        assert generate_diff(plain.render, YAML1_TREE, YAML2_TREE) == EXP_PLAIN


class TestPaths:
    def test_relpath(self):
        assert generate_diff(json_render.render,
                             JSON1, JSON2) == EXP_JSON_RES

    def test_abspath(self):
        assert generate_diff(json_render.render,
                             os.path.abspath(JSON1), JSON2) == EXP_JSON_RES

    def test_abspath(self):
        assert generate_diff(json_render.render,
                             os.path.abspath(JSON1),
                             os.path.abspath(JSON2)) == EXP_JSON_RES

    def test_wrong_format(self):
        assert generate_diff(json_render.render, JSON1, 'test.txt') \
               == WRONG_FILE_FORMAT_ERROR


class TestFormat:
    def test_wrong_format(self):
        assert generate_diff(None, JSON1, JSON2) == WRONG_OUTPUT_FORMAT_ERROR
