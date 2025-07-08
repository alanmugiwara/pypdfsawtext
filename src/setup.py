import sys
import platform
from cx_Freeze import setup, Executable

# Constantes pra unificar o setup
PKG = ["os", "sys", "subprocess", "platform", "webbrowser", "threading", "ocrmypdf", "customtkinter"]
APP_NAME = "PyPDF Saw Text"
APP_VERSION = "0.8.0.1"
APP_DESC = "Convert PDF-OCR (PT-BR)"

# lista vazia pra receber os parâmetros mutáveis de cada SO
executables = []

if platform.system() == "Windows":
    # Caminhos dos binários instalados no Windows
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    tessdata_path = r"C:\Program Files\Tesseract-OCR\tessdata"
    ghostscript_path = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"
    ghostscript_path_dll = r"C:\Program Files\gs\gs10.05.1\bin\gsdll64.dll"
    ghostscript_path_lib = r"C:\Program Files\gs\gs10.05.1\bin\gsdll64.lib"

    build_exe_options = {
        "packages": PKG,
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
    # Chamada da lista com definições de Windows
    executables = [Executable("main.py", base=base, icon="icon.ico")]

elif platform.system() == "Linux":
    build_exe_options = {
        "packages": PKG
    }
    # Chamada da lista com definições de linux
    executables = [Executable("main.py")]

else:
    print("Sistema não suportado!")
    sys.exit(1)

# Chamada de setup unificada
setup(
    name=APP_NAME,
    version=APP_VERSION,
    description=APP_DESC,
    options={"build_exe": build_exe_options},
    executables=executables
    )