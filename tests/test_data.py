first_file = {
    "Person": {
        "isAdmin": True,
        "name": "Harry",
        "age": 15,
        },
    "group": {
        "Skills": "Engineer",
        "nothing": {
            "else": "matters"
        }
        }
    }

second_file = {
    "Person": {
        "isAdmin": False,
        "name": "Harry",
        "age": 15,
        },
    "group": {
        "good": {
            "guys": "... twice"
        }
        },
    "test": 9999
    }

raw_diff = {
    'test': {
        'value': 9999,
        'status': 'added'
    },
    'group': {
        'value': {
            'good': {
                'value': {
                    'guys': {
                        'value': '... twice'
                    }
                },
                'status': 'added'
            },
            'Skills': {
                'value': 'Engineer',
                'status': 'removed'
            },
            'nothing': {
                'value': {
                    'else': {
                        'value': 'matters'
                    }
                },
                'status': 'removed'
            }
        },
        'status': 'complex value'
    },
    'Person': {
        'value': {
            'age': {
                'value': 15,
                'status':
                    'unchanged'
            },
            'name': {
                'value': 'Harry',
                'status': 'unchanged'
            },
            'isAdmin': {
                'old_value': True,
                'new_value': False,
                'status': 'changed'
            }
        },
        'status': 'complex value'
    }
}
