from gendiff import engine


def render(node, level=1):
    result = []
    sign = '    ' * level
    added = '{}+ '.format(sign[:-2])
    removed = '{}- '.format(sign[:-2])
    for key, val in sorted(node.items()):
        value = val.get(engine.VALUE)
        status = val.get(engine.STATUS)
        if isinstance(value, dict) and status != engine.COMPLEX_VALUE:
            value = render(value, level + 1)
        new_meta = '{}: {}'.format(key, value)
        if status == engine.ADDED:
            result.append(added + new_meta)
        elif status == engine.REMOVED:
            result.append(removed + new_meta)
        elif status == engine.CHANGED:
            result.append('{}{}: {}'.format(removed,
                                            key,
                                            val[engine.OLD_VALUE]
                                            ))
            result.append('{}{}: {}'.format(added,
                                            key,
                                            val[engine.NEW_VALUE]))
        elif status == engine.UNCHANGED:
            result.append(sign + new_meta)
        elif status == engine.COMPLEX_VALUE:
            value = render(value, level + 1)
            result.append('{}{}: {}'.format(sign, key, value))
        else:
            result.append(sign + new_meta)
    return '{' + '\n' + ('\n'.join(result)) + '\n' \
           + '   ' * (level - 1) + '}'
