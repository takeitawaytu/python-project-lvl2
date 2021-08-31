from gendiff.renders import json_render, plain
import json

FORMAT = {
    'json': json.dumps,
    'stylish': json_render.render,
    'plain': plain.render
}
