from flask import request, jsonify, flash

from app import get_logger, get_config
from . import main
from os import path

logger = get_logger(__name__)
cfg = get_config()


@main.route('/api/project/config', methods=['GET'])
def read_config():
    """
    :path_param path: the path of config file to read
    :return: {
        "config_content": "String with '\n'"
    }
    """
    file = request.args.get("path")
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


@main.route('/api/project/config', methods=['POST'])
def write_config():
    """
    :path_param path: the path of config file to read
    :json_content {
        "config_content": "String with '\n'"
    }
    :return:
    """
    file = request.args.get("path", "resources/file3.txt")
    content = request.json["config_content"]
    print(content)

    abspath = path.abspath(file)
    print(abspath)

    with open(abspath, 'w') as config_file:
        config_file.write(content)
    flash("Config is Saved!")
    return "Config is Saved!", 201
