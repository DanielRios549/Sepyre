from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Main():
    main: Sepyre
    page: app.flet.Page

    def __post_init__(self):
        self.page.title = 'Sepyre'
        self.page.appbar = AppBar(
            leading=app.flet.IconButton(
                bgcolor=colors.SURFACE_VARIANT,
                icon=icons.MENU
            ),
            leading_width=40,
            title=Text("Library"),
            center_title=False,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                IconButton(icons.WB_SUNNY_OUTLINED),
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Autoplay", on_click=self.item_clicked)
                    ]
                ),
            ],
        )

        self.tabs: Tabs
        self.songs = app.pages.Songs(self.main, self.page)
        self.playlists = app.pages.Playlists(self.main, self.page)

        self.tabIndexes: list[app.pages.Page] = [  # type: ignore
            self.songs, self.playlists
        ]

        self.tab1 = Tab(
            text='Songs',
            content=self.songs.show()
        ),
        self.tab2 = Tab(
            text='Playlist',
            content=self.playlists.show()
        )

        self.page.add(
            self.showTabs()
        )

    def item_clicked(self, event):  # : event.ControlEvent):
        event.control.checked = not event.control.checked
        self.page.update()

    def editSongs(self):
        index = self.tabs.selected_index
        self.tabs.tabs[index].content = self.tabIndexes[index].showEdit()
        self.page.update()

    def showTabs(self):
        self.tabs = Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                self.tab1[0],
                self.tab2
            ],
            expand=1,
        )

        return self.tabs
