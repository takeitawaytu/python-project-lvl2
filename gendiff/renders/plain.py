from gendiff import engine


def render(node, level=''):
    result = []
    for key, val in sorted(node.items()):
        value = val.get(engine.VALUE)
        status = val.get(engine.STATUS)
        if status == engine.ADDED:
            if isinstance(value, dict):
                value = engine.COMPLEX_VALUE
            result.append('Property \'{}{}\' was added with value \'{}\''
                          .format(level, key, value))
        elif status == engine.REMOVED:
            result.append('Property \'{}{}\' was removed'
                          .format(level, key))
        elif status == engine.CHANGED:
            result.append('Property \'{}{}\' was changed. From \'{}\' to \'{}\''
                          .format(level, key,
                                  val[engine.OLD_VALUE],
                                  val[engine.NEW_VALUE]))
        elif status == engine.COMPLEX_VALUE:
            level += key + '.'
            result.append(render(value, level))
            level = ''
    return '\n'.join(result)
