from gendiff import engine
from gendiff.renders.json_render \
    import get_lower, get_value


def make_converted(node):
    if isinstance(node, dict):
        return '[complex value]'
    elif isinstance(node, str):
        if node in ('null', 'true', 'false'):
            return '{}'.format(node)
        return '\'{}\''.format(node)
    return get_lower(node)


def render(node, level=''):
    result = []
    for key, val in sorted(node.items()):
        status, value = get_value(val)
        converted = make_converted(value)
        if status == engine.ADDED:
            result.append('Property \'{}{}\' was added with value: {}'
                          .format(level, key, converted))
        elif status == engine.REMOVED:
            result.append('Property \'{}{}\' was removed'
                          .format(level, key))
        elif status == engine.CHANGED:
            result.append('Property \'{}{}\' was updated. From {} to {}'
                          .format(level, key,
                                  make_converted(val[engine.OLD_VALUE]),
                                  make_converted(val[engine.NEW_VALUE])
                                  ))
        elif status == engine.COMPLEX_VALUE:
            result.append(render(value, level + '{}.'.format(key)))
    return '\n'.join(result)
