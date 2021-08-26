import json
import yaml

LOADERS = {
    '.yml': yaml.load,
    '.yaml': yaml.load,
    '.json': json.load
}
