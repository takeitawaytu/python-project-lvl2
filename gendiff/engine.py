STATUS = 'status'
ADDED = 'added'
REMOVED = 'removed'
CHANGED = 'changed'
UNCHANGED = 'unchanged'
VALUE = 'value'
COMPLEX_VALUE = 'complex value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'


def object_value(node):
    if isinstance(node, dict):
        result = {}
        for key, value in node.items():
            if isinstance(value, dict):
                result.update({key: {VALUE: object_value(value)}})
            else:
                result.update({key: {VALUE: value}})
    else:
        result = node
    return result


def find_diff(dict1, dict2):
    result = {}
    old_keys = dict1.keys()
    new_keys = dict2.keys()
    for key in (new_keys - old_keys):
        result.update({key: {VALUE: object_value(dict2[key]), STATUS: ADDED}})
    for key in (old_keys - new_keys):
        result.update({key: {VALUE: object_value(dict1[key]), STATUS: REMOVED}})
    for key in old_keys & new_keys:
        old_value = dict1[key]
        new_value = dict2[key]
        if old_value == new_value:
            result.update({key: {VALUE: new_value, STATUS: UNCHANGED}})
        else:
            if isinstance(old_value, dict) and isinstance(new_value, dict):
                result.update({key: {VALUE: find_diff(old_value, new_value),
                                     STATUS: COMPLEX_VALUE}})
            else:
                result.update({key: {OLD_VALUE: old_value, NEW_VALUE: new_value,
                                     STATUS: CHANGED}})
    return result
