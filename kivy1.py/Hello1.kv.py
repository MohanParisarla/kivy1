

from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton

class PositionApp(MDApp):
    def build(self):
        layout = FloatLayout()

        # Top Left
        top_left = MDRaisedButton(text="Top Left",
                                  size_hint=(None, None),
                                  size=("100dp", "50dp"),
                                  pos_hint={"x": 0, "top": 1})
        layout.add_widget(top_left)

        # Top Right
        top_right = MDRaisedButton(text="Top Right",
                                   size_hint=(None, None),
                                   size=("100dp", "50dp"),
                                   pos_hint={"right": 1, "top": 1})
        layout.add_widget(top_right)

        # Bottom Left
        bottom_left = MDRaisedButton(text="Bottom Left",
                                     size_hint=(None, None),
                                     size=("100dp", "50dp"),
                                     pos_hint={"u": 1, "top": 0})
        layout.add_widget(bottom_left)

        # Bottom Right
        bottom_right = MDRaisedButton(text="Bottom Right",
                                      size_hint=(None, None),
                                      size=("100dp", "50dp"),
                                      pos_hint={"right": 1, "y": 0})
        layout.add_widget(bottom_right)

        # Center
        center = MDRaisedButton(text="Center",
                                size_hint=(None, None),
                                size=("100dp", "50dp"),
                                pos_hint={"center_x": 0.5, "center_y": 0.5})
        layout.add_widget(center)

        return layout

PositionApp().run()
