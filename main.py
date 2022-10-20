#!/usr/bin/env python3
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("ui_dig_ver.glade")

class Manipulador:
    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_button_dig_ver_clicked(self, button):
        codigo = builder.get_object("entry_codigo").get_text()
        self.calcularDV(codigo)

    def calcularDV(self, numero):
        pass

    def mensagem(self, param, param1, param2):
        pass

builder.connect_signals(Manipulador())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
