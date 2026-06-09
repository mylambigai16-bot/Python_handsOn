from configparser import ConfigParser

def get_config(category, key):
    con = ConfigParser()
    con.read("Python_selenium/TutorialsNinja/config.ini")
    return con.get(category, key)
