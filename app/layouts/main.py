from dataclasses import dataclass
from main import Sepyre
from app.flet import *


@dataclass()
class Main():
    main: Sepyre

    def __post_init__(self):
        pass

    def appBar(self, title: str = 'Sepyre'):
        width = 50

        return AppBar(
            toolbar_height=width,
            bgcolor=colors.SURFACE_VARIANT,
            leading_width=width,
            leading=IconButton(
                bgcolor=colors.SURFACE_VARIANT,
                icon=icons.MENU
            ),
            title=TextButton(
                title,
                scale=1.5,
                on_click=lambda x: self.main.page.go('/')
            ),
            center_title=False,
            actions=[
                IconButton(icons.WB_SUNNY_OUTLINED, width=width),
                PopupMenuButton(
                    width=width,
                    items=[
                        PopupMenuItem(text="Autoplay")  # , on_click=self.item_clicked)
                    ]
                ),
            ],
        )

    def navRail(self):
        return NavigationRail(
            selected_index=0,
            label_type="all",
            # extended=True,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="First"
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.BOOKMARK_BORDER),
                    selected_icon_content=Icon(icons.BOOKMARK),
                    label="Second",
                ),
                NavigationRailDestination(
                    icon=icons.SETTINGS_OUTLINED,
                    selected_icon_content=Icon(icons.SETTINGS),
                    label_content=Text("Settings"),
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        )
