from gendiff import engine


def get_lower(value):
    if value is None:
        lowered_value = 'null'
    elif value is True:
        lowered_value = 'true'
    elif value is False:
        lowered_value = 'false'
    else:
        lowered_value = value
    return lowered_value


def complex_value_render(node, level):
    if isinstance(node, dict):
        return render(node, level + 1)
    return get_lower(node)


def get_value(node):
    if isinstance(node, dict):
        return node.get(engine.STATUS), node.get(engine.VALUE)
    return None, get_lower(node)


def render(node, level=1):  # noqa: C901
    result = []
    sign = '    ' * level
    added = '{}+ '.format(sign[:-2])
    removed = '{}- '.format(sign[:-2])
    for key, val in sorted(node.items()):
        status, value = get_value(val)
        if isinstance(value, dict) and status != engine.COMPLEX_VALUE:
            value = render(value, level + 1)
        new_meta = '{}: {}'.format(key, get_lower(value))
        if status == engine.ADDED:
            result.append(added + new_meta)
        elif status == engine.REMOVED:
            result.append(removed + new_meta)
        elif status == engine.CHANGED:
            result.append('{}{}: {}'.format(removed,
                                            key,
                                            complex_value_render(
                                                val[engine.OLD_VALUE], level)
                                            ))
            result.append('{}{}: {}'.format(added,
                                            key,
                                            complex_value_render(
                                                val[engine.NEW_VALUE], level)
                                            ))
        elif status == engine.UNCHANGED:
            result.append(sign + new_meta)
        elif status == engine.COMPLEX_VALUE:
            value = render(value, level + 1)
            result.append('{}{}: {}'.format(sign, key, value))
        else:
            result.append(sign + new_meta)
    return '{' + '\n' + ('\n'.join(result)) + '\n' \
           + '    ' * (level - 1) + '}'
