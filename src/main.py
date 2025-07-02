import os
import sys
import subprocess
import platform
import webbrowser
import threading
import ocrmypdf
import customtkinter as ctk
from customtkinter import filedialog

# Detecta se está rodando como EXE (build) ou como script
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

# Garante que o Tesseract e o Ghostscript venham da pasta local "bin"
bin_path = os.path.join(base_path, "bin")
os.environ["PATH"] = bin_path + os.pathsep + os.environ.get("PATH", "")

# Define onde estão os dados de linguagem do Tesseract
os.environ["TESSDATA_PREFIX"] = os.path.join(base_path, "tessdata")

# Força o ocrmypdf a usar caminhos específicos:
os.environ["OCRMYPDF_TESSERACT"] = os.path.join(bin_path, "tesseract.exe")
os.environ["OCRMYPDF_GHOSTSCRIPT"] = os.path.join(bin_path, "gs.exe")

# Inicializa as variáveis globais pxra evitar erro
in_folder = ""
out_folder = ""
pdfs = []

# Oculta janelas de terminal
if platform.system() == "Windows":
    original_popen = subprocess.Popen

    def hidden_popen(*args, **kwargs):
        kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
        return original_popen(*args, **kwargs)

    subprocess.Popen = hidden_popen

def input_folder():
    global in_folder
    in_folder = filedialog.askdirectory()
    if not in_folder:
        label_status.configure(text="Nenhuma pasta de entrada foi selecionada!")
        return
    
def output_folder():
    global out_folder, pdfs, in_folder
    out_folder = filedialog.askdirectory()
    if not out_folder:
        label_status.configure(text="Nenhuma pasta de saída foi selecionada!")
        return
    
    global pdfs
    pdfs = []
    for file in os.listdir(in_folder):
        if file.lower().endswith(".pdf"):
            pdfs.append(file)

def web_link(event=None):
    webbrowser.open_new("https://github.com/alanmugiwara")  

# Conversão e spinner de status
def convert_pdfs():
    global pdfs, in_folder, out_folder

    if not in_folder:
        label_status.configure(text='Selecione a pasta de origem primeiro!')
        return
    
    if not out_folder:
        label_status.configure(text='Selecione a pasta de de destino primeiro!')
        return
    
    if not pdfs:
        label_status.configure(text='Nenhum arquivo PDF encontrado!')
        return
    
    label_status.configure(text='Fazendo a mágica acontecer\nPor favor, aguarde...')
    label_status.pack(pady=(0, 10)) # espaçamento | texto

    label_emoji = ctk.CTkLabel(
    window,
    text="🧙‍♂️",
    font=("Segoe UI Emoji", 45) 
    )

    label_emoji.pack(pady=(5, 5)) # espaçamento | emoji

    spinner.pack(pady=(5)) 
    spinner.start()

    for pdf in pdfs:
        entrada = os.path.join(in_folder, pdf)
        saida = os.path.join(out_folder, f"pesquisavel_{pdf}")
        try:
            ocrmypdf.ocr(entrada, saida, lang="por")
        except Exception as e:
            spinner.stop()
            spinner.pack_forget()
            label_status.configure(text=f"Erro ao processar {pdf}:\n{e}")
            return
    
    spinner.stop()
    spinner.pack_forget()
    label_status.configure(text="Conversão concluída com sucesso!")

# setup visual
ctk.set_appearance_mode('dark')

# setup da janela
window= ctk.CTk()
window.geometry('420x400')
window.title('PyPDF Saw Text - Aplique OCR em seus PDFs!')

# Botão de entrada
botao_in = ctk.CTkButton(window, text='Selecione a pasta de origem', command=input_folder)
botao_in.pack(pady=20)

# Botão de saída
botao_out = ctk.CTkButton(window, text='Selecione a pasta de destino', command=output_folder)
botao_out.pack(pady=10)

# Botão de conversão
botao_convert = ctk.CTkButton(window, text="Converter PDFs", command=lambda: threading.Thread(target=convert_pdfs, daemon=True).start())
botao_convert.pack(pady=30)

# Setup do tatus textual
label_status = ctk.CTkLabel(window, text="", wraplength=400, justify="center")
label_status.pack(pady=10)

# setup do Spinner
spinner = ctk.CTkProgressBar(window, mode='indeterminate')
spinner.pack_forget()

# Container do rodapé
footer_frame = ctk.CTkFrame(window, fg_color="transparent")
footer_frame.pack(side="bottom", padx=110, pady=10)

# Créditos à esquerda
label_by = ctk.CTkLabel(footer_frame, text="By Álan Cruz | ")
label_by.pack(side="left")

# Link à direita
link_rodape = ctk.CTkLabel(footer_frame, text="Visite meu GitHub", cursor="hand2")
link_rodape.pack(side="right")
link_rodape.bind("<Button-1>", web_link)

# instância da janela
window.mainloop()