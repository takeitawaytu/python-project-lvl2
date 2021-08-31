from gendiff.engine import find_diffs
from gendiff.app import generate_diff, read_file,\
    WRONG_FILE_FORMAT_ERROR, WRONG_OUTPUT_FORMAT_ERROR
from gendiff.renders import json_render, plain
from tests import input_data
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
JSON_PLAIN_RES = 'tests/fixtures/plain_res'
YAML_PLAIN_RES = 'tests/fixtures/yaml_tree_res_plain'
EXP_JSON_RES = get_file_content(JSONTXT_RES)
EXP_YAML_RES = get_file_content(YAML_RES)
EXP_JSON_RES_TREE = get_file_content(JSONTXT_RES_TREE)
EXP_YAML_RES_TREE = get_file_content(YAML_RES_TREE)
EXP_JSON_PLAIN = get_file_content(JSON_PLAIN_RES)
EXP_YAML_PLAIN = get_file_content(YAML_PLAIN_RES)


class TestJSON:
    @pytest.mark.parametrize('data1,data2,exp_res',
                             [(input_data.first_file1,
                               input_data.second_file1,
                               input_data.raw_diff1),
                              (input_data.first_file2,
                               input_data.second_file2,
                               input_data.raw_diff2)])
    def test_find_diff(self, data1, data2, exp_res):
        diff = find_diffs(data1, data2)
        assert diff == exp_res

    def test_render_diffs(self):
        assert json_render.render(input_data.raw_diff1) == EXP_JSON_RES

    def test_render_diffs_tree(self):
        assert generate_diff(JSON1_TREE, JSON2_TREE,
                             'stylish') == EXP_JSON_RES_TREE


class TestYaml:
    def test_yml_and_yaml(self):
        assert generate_diff(YAML1, YAML2,
                             'stylish') == EXP_YAML_RES

    def test_yml_and_yaml_tree(self):
        assert generate_diff(YAML1_TREE, YAML2_TREE,
                             'stylish') == EXP_YAML_RES_TREE
        assert generate_diff(YAML1_TREE, YAML2_TREE, 'stylish') == EXP_YAML_RES_TREE


class TestPlain:
    def test_plain_json(self):
        assert generate_diff(JSON1_TREE, JSON2_TREE,
                             'plain') == EXP_JSON_PLAIN

    def test_plain_yaml(self):
        assert generate_diff(YAML1_TREE, YAML2_TREE,
                             'plain') == EXP_YAML_PLAIN


class TestPaths:
    def test_relpath(self):
        assert generate_diff(JSON1, JSON2, 'stylish') == EXP_JSON_RES

    def test_abs_relpath(self):
        assert generate_diff(os.path.abspath(JSON1), JSON2,
                             'stylish') == EXP_JSON_RES

    def test_abspath(self):
        assert generate_diff(os.path.abspath(JSON1),
                             os.path.abspath(JSON2),
                             'stylish') == EXP_JSON_RES

    def test_wrong_format(self):
        assert generate_diff(JSON1, 'test.txt',
                             'stylish') == WRONG_FILE_FORMAT_ERROR


class TestFormat:
    def test_generate_diff_only_path(self):
        assert generate_diff(JSON1, JSON2) == EXP_JSON_RES
