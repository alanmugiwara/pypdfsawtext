# setup_win.py
# FIX Tcl error on win, run "$env:TCL_LIBRARY = "C:\Users/%username%\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"

import sys
import os
from cx_Freeze import setup, Executable

# Caminhos dos binários instalados no Windows
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tessdata_path = r"C:\Program Files\Tesseract-OCR\tessdata"
ghostscript_path = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"
ghostscript_path_dll = r"C:\Program Files\gs\gs10.05.1\bin\gsdll64.dll"
ghostscript_path_lib = r"C:\Program Files\gs\gs10.05.1\bin\gsdll64.lib"

# Definição de dependências que serão empacotadas
build_exe_options = {
    "packages": ["os", "sys", "subprocess", "platform", "webbrowser", "threading", "ocrmypdf", "customtkinter"],
    "include_files": [
        (tesseract_path, "bin/tesseract.exe"),
        (ghostscript_path, "bin/gswin64c.exe"),
        (ghostscript_path_dll, "bin/gsdll64.dll"),
        (ghostscript_path_lib, "bin/gsdll64.lib"),
        (tessdata_path, "tessdata"),
        "icon.ico",
    ],
    "include_msvcr": False
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="PyPDF Saw Text",
    version="1.0",
    description="Convert PDF com OCR-PtBr",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="icon.ico")]
)