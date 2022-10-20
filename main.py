#!/usr/bin/env python3
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("ui_dig_ver.glade")

MULTIPLICADORES = (8, 6, 4, 2, 3, 5, 9, 7)


class Manipulador:
    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_button_dig_ver_clicked(self, button):
        codigo = builder.get_object("entry_codigo").get_text()
        self.calcularDV(codigo)

    def calcularDV(self, numero):
        digito = builder.get_object("lbl_digito_ver")
        try:
            dv = 0
            if len(numero) == 8:
                for i, v in enumerate(numero):
                    dv = dv + (int(numero[i]) * MULTIPLICADORES[i])
                dv = dv * 10
                dv = dv % 11
                if dv == 0:
                    digito.set_text('"5"')
                elif dv == 10:
                    digito.set_text('"0"')
                else:
                    digito.set_text(str(f'"{dv}"'))
            else:
                self.mensagem('ERRO', 'O código de rastreamento precisa ter 8 (oito) dígitos numéricos', 'dialog-error')
                digito.set_text('')
        except Exception:
            self.mensagem('ERRO', 'O código de rastreamento precisa ter 8 (oito) dígitos numéricos', 'dialog-error')

    def mensagem(self, param, param1, param2):
        message: Gtk.MessageDialog = builder.get_object('mensagem')
        message.props.text = param
        message.props.secondary_text = param1
        message.props.icon_name = param2
        message.show_all()
        message.run()
        message.hide()

builder.connect_signals(Manipulador())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
