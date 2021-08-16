from gendiff.scripts import gendiff


def render(node, level=1):
    result = []
    sign = '    ' * level
    added = '{}+ '.format(sign[:-2])
    removed = '{}- '.format(sign[:-2])
    for key, val in sorted(node.items()):
        value = val.get(gendiff.VALUE)
        status = val.get(gendiff.STATUS)
        if isinstance(value, dict) and status != gendiff.COMPLEX_VALUE:
            value = render(value, level + 1)
        new_meta = '{}: {}'.format(key, value)
        if status == gendiff.ADDED:
            result.append(added + new_meta)
        elif status == gendiff.REMOVED:
            result.append(removed + new_meta)
        elif status == gendiff.CHANGED:
            result.append('{}{}: {}'.format(removed, key, val[gendiff.OLD_VALUE]))
            result.append('{}{}: {}'.format(added, key, val[gendiff.NEW_VALUE]))
        elif status == gendiff.UNCHANGED:
            result.append(sign + new_meta)
        elif status == gendiff.COMPLEX_VALUE:
            value = render(value, level + 1)
            result.append('{}{}: {}'.format(sign, key, value))
        else:
            result.append(sign + new_meta)
    return '{' + '\n' + ('\n'.join(result)) + '   ' * (level - 1) + '\n' + '}'

