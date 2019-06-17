# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:45:53 2018

@author: srikanth
"""

from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label

class Simplekivy(App):
    def build(self):
        return Label()
    
if __name__=='__main__':
    Simplekivy().run()