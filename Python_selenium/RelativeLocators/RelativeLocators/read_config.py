from configparser import ConfigParser
import os

def get_config(category, key):
    con = ConfigParser()

    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "Config.ini"
    )

    con.read(config_path)

    return con.get(category, key)