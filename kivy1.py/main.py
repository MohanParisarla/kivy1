from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Color, Line

Window.size = (360, 550)

navigation_helper = """
MDNavigationLayout:

    ScreenManager:
        Screen:

            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Demo Application"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                    elevation: 1

                ScrollView:
                    MDBoxLayout:
                          
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        padding: "20dp","16dp"
                        spacing: "13dp"
                        pos_hint: {"center_y": .5}
                        
                        
                        Image:
                            source: "demoq.jpg"
                            size_hint_y: None
                            height:"150dp"
                            
                           
                        Image:
                            source: "demoq.jpg"
                            size_hint_y: None
                            height: "150dp"

                        Image:
                            source: "demoq.jpg"
                            size_hint_y: None
                            height: "150dp"

    MDNavigationDrawer:
        id: nav_drawer

        BoxLayout:
            orientation: 'vertical'
            padding: '8dp'
            spacing: '8dp'

            Image:
                source: "demoq.jpg"
                size_hint: (1, None)
                height: "150dp"

            MDLabel:
                text: "   Demo User"
                font_style: "Subtitle1"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "   demo@example.com"
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "YouTube"
                        IconLeftWidget:
                            icon: "youtube"

                    OneLineIconListItem:
                        text: "Upload"
                        IconLeftWidget:
                            icon: "folder"

                    OneLineIconListItem:
                        text: "Logout"
                        IconLeftWidget:
                            icon: "logout"
"""

class DemoApplication(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"

        return Builder.load_string(navigation_helper)

DemoApplication().run()
