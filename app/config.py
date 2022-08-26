from configparser import ConfigParser
from dataclasses import dataclass
from main import Sepyre
import app


@dataclass()
class Config():
    main: Sepyre

    def __post_init__(self):
        self.separation = self.main.folder.joinpath('separation')
        userFolder = self.main.home

        self.folder = userFolder.joinpath(self.main.options['folder'])
        self.file = self.folder.joinpath(self.main.options['file'])
        self.initialSettings = False

        if self.folder.exists() is False:
            print(f'Creating Config Folder at \033[34m{self.folder}\033[m...')
            self.folder.mkdir(0o775, False, False)
            self.initialSettings = True

        if self.file.exists() is False:
            print(f'Creating Config File at \033[34m{self.file}\033[m...')
            self.file.touch(0o775, False)
            self.initialSettings = True

    def getAll(self) -> dict:
        return app.parser.config(str(self.file))

    def get(self, section: str, config: str, default: str) -> str:
        if section == 'env':
            return self.main.options[config]
        else:
            configs = self.getAll()

            if section in configs.keys() and config in configs[section]:
                return configs[section][config]
            else:
                return default

    def update(self, section: str, key: str, value: str):
        configFile = str(self.file)
        parser = ConfigParser()
        parser.read(configFile)

        if section not in parser.sections():
            parser.add_section(section)

        parser.set(section, key, value)

        with open(configFile, 'w+') as config:
            parser.write(config)
