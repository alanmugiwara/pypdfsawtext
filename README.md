[![made With](https://img.shields.io/badge/Made%20with-Python%20-8A2BE2)](https://github.com/alanmugiwara)
![Created](https://img.shields.io/badge/Created-Jul%202,%202025-8A2BE2)
[![Last Commit](https://img.shields.io/github/last-commit/alanmugiwara/pypdfsawtext?color=8A2BE2&label=Last%20Commit)](https://github.com/alanmugiwara/alanmugiwara)
[![contributors](https://img.shields.io/github/contributors/alanmugiwara/pypdfsawtext?color=8A2BE2&label=Contributors)](https://github.com/alanmugiwara)
[![issues counter](https://img.shields.io/github/issues/alanmugiwara/pypdfsawtext?color=8A2BE2&label=Issues)](https://github.com/alanmugiwara)
[![repo size](https://img.shields.io/github/repo-size/alanmugiwara/pypdfsawtext?color=8A2BE2&label=Repo%20Size)](https://github.com/alanmugiwara)
[![files counter](https://img.shields.io/github/directory-file-count/alanmugiwara/pypdfsawtext?color=8A2BE2&label=Files%20Counter)](https://github.com/alanmugiwara)
[![Latest Tag](https://img.shields.io/github/v/tag/alanmugiwara/pypdfsawtext?color=8A2BE2&label=Last%20Tag)](https://github.com/alanmugiwara/pypdfsawtext/releases)
[![downloads counter](https://img.shields.io/github/downloads/alanmugiwara/pypdfsawtext/total?color=8A2BE2&label=Downloads)](https://github.com/alanmugiwara)
[![Maintainability](https://qlty.sh/badges/f983cb35-d208-4d2f-8872-03fb3e1205de/maintainability.svg)](https://qlty.sh/gh/alanmugiwara/projects/pypdfsawtext)
[![Code Coverage](https://qlty.sh/badges/f983cb35-d208-4d2f-8872-03fb3e1205de/test_coverage.svg)](https://qlty.sh/gh/alanmugiwara/projects/pypdfsawtext)

# PyPDF Text View
PyPDF Text View é uma aplicação desktop escrita em Python que insere a tecnologia OCR (Optical Character Recognition – Reconhecimento Óptico de Caracteres) em documentos no formato PDF.
A ferramenta permite que o usuário selecione uma pasta contendo arquivos PDF e, de forma automatizada, converta todos os documentos encontrados em versões com texto pesquisável. E não há limite predefinido de arquivos: todos os PDFs válidos encontrados na pasta selecionada serão processados sequencialmente.
## 📥 Download

<a href="https://github.com/alanmugiwara/pypdfsawtext/releases/latest">
  <img src="https://github.com/gokadzev/Musify/raw/master/repository_files/get-it-on-github.png" alt="Get it on GitHub" width="200"/>
</a>

- ✅ **Não é necessário ter Python instalado. O interpretador está incluso!**
- ⚠️ **O Tesseract e Ghostscript já estão embutidos na pasta `bin/` do executável**.

## Funcionalidades
- **Definir pasta de origem dos documentos:** Permite escolher a pasta que contém todos os arquivos PDF a serem convertidos, sem limite máximo de documentos;
- **Definir pasta de saída dos documentos:** Define o local onde os arquivos convertidos serão salvos. Os PDFs manterão os mesmos nomes dos arquivos originais, sem a necessidade de renomeá-los manualmente;
- **Acesso ao repositório do desenvolvedor:** Um link localizado no rodapé da aplicação direciona diretamente para este repositório;
- **Reconhecimento Óptico de Caracteres (OCR):**  O texto dos documentos será reconhecido em Português (Brasil) utilizando a tecnologia do Tesseract;
- **Compressão:** O novo PDF tende a ocupar menos espaço em disco. Já que a ferramenta utiliza o Ghostscript para comprimir imagens e dados internos do arquivo, sem alterar seu conteúdo.

## Tecnologias Utilizadas
- **Python 3.13.0:** Linguagem de programação utilizada;
- **CustomTkinter:** Biblioteca que cria a interface gráfica;
- **ocrmypdf:** Biblioteca que extrai as páginas do PDF como imagens;
- **Tesseract OCR:** Ferramenta OpenSource que usa OCR para converter as imagens em texto reconhecível;
- **Ghostscript:** Para reescrever um novo PDF válido e com tamanho otimizado;
- **cx_Freeze:** Biblioteca que cria versões executáveis da aplicação para diferentes arquiteturas

# Demonstração 
![Demonsraoção](https://github.com/alanmugiwara/alanmugiwara.github.io/blob/main/img/demo-pysawtext.gif?raw=true)

## Como Reproduzir?

1. **Clone este repositório usando comando abaixo:**

```bash
git clone https://github.com/alanmugiwara/pypdfsawtext
```

2.  **Navegue até o diretório /src:**
   ```bash
   cd pypdfsawtext/src
   ```

3. **Instale todas as dependências de Python necessárias:**
```bash     
pip install -r requirements.txt
```

4. **Instale as dependências necessárias para a aplicação:**

#### *Windows*
- [Ghostscript/GhostPDL 10.05.1](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/tag/gs10051)
- [tesseract-ocr/tesseract · v5.5.0.20241111](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0)


5. **Execute o Programa:**
```bash
python main.py
 ```

## Como Compilar uma versão executável?

1. **Clone este repositório usando comando abaixo:**

```bash
git clone https://github.com/alanmugiwara/pypdfsawtext
```

2. **Instale as dependências necessárias para a aplicação:**

#### *Windows*
- [Ghostscript/GhostPDL 10.05.1](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/tag/gs10051)
- [tesseract-ocr/tesseract · v5.5.0.20241111](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0)


3.  **Navegue até o diretório /src:**
```bash
cd pypdfsawtext/src
```

4.  *Windows* - **Rode o comando abaixo para compilar:**
```bash
python setup_win.py build_exe
```
