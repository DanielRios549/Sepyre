from dataclasses import dataclass
from configparser import ConfigParser
from main import Sepyre
from app.flet import *


@dataclass()
class FormAdd():
    main: Sepyre

    def __post_init__(self):
        self.info = Text()
        self.dialog = FilePicker(on_result=self.update)

        self.main.page.overlay.append(self.dialog)

    def show(self):
        return Row(
            controls=[
                ElevatedButton(
                    "Add Songs",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: self.dialog.pick_files(
                        allow_multiple=True,
                        file_type='audio'
                    ),
                ),
                self.info,
            ]
        )

    def update(self, event: FilePickerResultEvent):
        if not event.files:
            self.info.value = "Select at least one file"
        else:
            self.info.value = ""
            # self.info.value = (
            #     ", ".join(map(lambda file: file.name, event.files)) if event.files else "Select at least one file"
            # )
            # folder = self.main.config.separation.joinpath(self.).mkdir(0o775, False, False)

            for file in event.files:
                extension = file.name.rfind('.')
                folder = file.name.replace(' ', '-')[:extension].lower()

                path = self.main.config.separation.joinpath(folder)
                path.mkdir(0o775, False, False)

                info = path.joinpath('info.conf')
                info.touch(0o775, False)

                self.main.config.update('info', 'name', file.name[:extension], str(info))

        # TODO: Fix UI Refresh
        self.main.page.update()
        self.info.update()
