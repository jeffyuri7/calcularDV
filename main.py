#!/usr/bin/env python3

"""CalcularDV - A Gtk calculator.

Goal: Calculate the check digit for postal labels

Language: Python

GUI: GTK

Summary: This software calculate the check digit for postal labels. To do this,
you must enter the first eight numeric digits of the label, not including
letters.
This program calculates only labels that follow the international post pattern,
for example:
AB123456789CD.

Usage: To calculate the label check digit with the following: "AB123456789CD",
enter first eight numerics digits in input field. E.g. 12345678, and click the
Calcular button. The check digit will be shown on the Dígito Verificador label.

"""

import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')


builder = Gtk.Builder()
builder.add_from_file("ui_dig_ver.glade")

MULTIPLICADORES = (8, 6, 4, 2, 3, 5, 9, 7)


class Manipulador:
    """This class contains the operations used by the signal handler."""

    def on_main_window_destroy(self, window):
        """Terminates the program when the window is closed."""
        Gtk.main_quit()

    def on_button_dig_ver_clicked(self, button):
        """Triggers the calculateDV function."""
        codigo = builder.get_object("entry_codigo").get_text()
        self.calcularDV(codigo)

    def calcularDV(self, numero):
        """Calculate the check digit of the arg=numero."""
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
                self.mensagem('ERRO', 'O código de rastreamento precisa ter 8 \
                (oito) dígitos numéricos', 'dialog-error')
                digito.set_text('')
        except Exception:
            self.mensagem('ERRO', 'O código de rastreamento precisa ter 8 \
            (oito) dígitos numéricos', 'dialog-error')

    def mensagem(self, param, param1, param2):
        """Control of the messages."""
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
