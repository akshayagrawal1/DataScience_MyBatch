# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:15:35 2018

@author: srikanth
"""

#import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = 'UserName'))
        self.username = TextInput(multiline=True)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True,multiline=True)
        self.add_widget(self.password)
        
class myapp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    myapp().run()