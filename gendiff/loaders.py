import json
import yaml

LOADERS = {
    '.yml': yaml.safe_load,
    '.yaml': yaml.safe_load,
    '.json': json.load
}
