from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Main(app.types.Page):
    main: Sepyre

    def __post_init__(self):
        self.main.page.title = 'Sepyre'

        self.tabs: Tabs
        self.songs = app.pages.Songs(self.main)
        self.playlists = app.pages.Playlists(self.main)

        self.tabIndexes: list[app.pages.Page] = [  # type: ignore
            self.songs, self.playlists
        ]

    def show(self):
        self.main.layout.show(
            page=0,
            name='Library',
            body=[
                Tabs(
                    selected_index=0,
                    animation_duration=300,
                    expand=True,
                    tabs=[
                        Tab(
                            text='Songs',
                            content=self.songs.show()
                        ),
                        Tab(
                            text='Playlist',
                            content=self.playlists.show()
                        )
                    ],
                )
            ]
        )
        self.main.page.update()

    # def editSongs(self):
    #     index = self.tabs.selected_index
    #     self.tabs.tabs[index].content = self.tabIndexes[index].showEdit()
    #     self.main.page.update()
