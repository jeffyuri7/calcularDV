#!/usr/bin/env python3
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("ui_dig_ver.glade")

window = builder.get_object('main_window')
window.show_all()
Gtk.main()
