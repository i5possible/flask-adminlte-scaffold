from flask import request, jsonify

from app import get_logger, get_config
from . import main
from os import path

logger = get_logger(__name__)
cfg = get_config()


@main.route('/api/project/config', methods=['GET', 'POST'])
def p_config():
    file = request.args.get("path", "resources/file1.txt")
    print(file)
    abspath = path.abspath(file)
    print(abspath)
    print(path.isfile(file))
    lines = []
    with open(abspath, 'r') as config_file:
        for line in config_file.readlines():
            lines.append(line)
        print(lines)
    return jsonify({"config_content": "".join(lines)})
