#!/usr/bin/env python3

## Imports
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious
from kivy.uix.screenmanager import Screen

# KV File
with open("main.kv") as kv:
    Builder.load_string(kv.read())

# Main Class
class StdInApp(App):

    def developer(self, *args):
        self.Popup.open()

    def change_color(self, *args):
        colors = ["#FF0000","#00FF00","#0000FF","#FFFF00","#FF00FF","#00FFFF", "#FFFFFF"]
        color = "".join(random.choice(colors))
        if color == self.color_now:
            same = True
            while same:
                color = "".join(random.choice(colors))
                if color != self.color_now:
                    self.ScrollView.ids.colortext.foreground_color = color
                    self.color_now = color
                    same = False
        else:
            self.ScrollView.ids.colortext.foreground_color = color
            self.color_now = color

    # Build Method
    def build(self):
 
        self.color_now = "#FFFFFF"

        # Root
        root = Screen()

        # Action Bar
        self.ActionBar = ActionBar(
            )

        # Text Input
        self.ScrollView = ScrollView()

        # Popup
        self.Popup = Popup()

        # Add Widgets
        root.add_widget(self.ActionBar) 
        root.add_widget(self.ScrollView)

        # Color Change
        self.ActionBar.ids.textColor.on_press = self.change_color
        self.ActionBar.ids.dev.on_press = self.developer

        # Return Root
        return root

# Run
StdInApp().run()


# Developer: Kourva
