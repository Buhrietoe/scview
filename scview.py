#!/usr/bin/python
from gi.repository import Gtk

class MainWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="SCView")

w = MainWindow()
w.connect('delete-event', Gtk.main_quit)
w.show_all()
Gtk.main()