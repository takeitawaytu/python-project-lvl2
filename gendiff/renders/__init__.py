from . import json_render, plain
import json

FORMAT = {
    'json': json.dumps,
    'jsontxt': json_render.render
}
