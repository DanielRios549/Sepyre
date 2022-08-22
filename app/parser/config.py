from configparser import ConfigParser


def config(file: str, single: bool = False) -> dict:
    parser = ConfigParser()
    parser.read(file)

    options: dict = {}

    if single is False:
        for section in parser.sections():
            options[section] = {}

            for option, value in parser.items(section):
                options[section][option] = value
    else:
        for section in parser.sections():
            for option, value in parser.items(section):
                options[option] = value

    return options
