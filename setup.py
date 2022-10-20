#!/usr/bin/env python3

"""This module contains configuration functions to create an .exe file."""

import sys
from cx_Freeze import setup, Executable
from Dlls import include_files

base = None
if sys.platform == "win32":
    base = "Win32GUI"
if sys.platform == "win64":
    base = "Win64GUI"

setup(
    name="DV Etiqueta Postal",
    author="Jefferson Yuri (jeffyuri@hotmail.com)",
    version="1.0.0",
    description="Aplicativo para calcular o dígito verificador de etiquetas\
    postais com interface gráfica construída em GTK.",
    options={'build_exe': {
        'includes': ["gi"],
        'excludes': ["wx", "email", "pydoc_data", "curses"],
        'packages': ["gi"],
        'include_files': include_files
    }},
    executables=[
        Executable("main.py",
                   base=base,
                   icon="static/images/icone2.ico",
                   shortcut_name="DV Etiqueta Postal",
                   shortcut_dir="DesktopFolder"
                   )
    ]
)
