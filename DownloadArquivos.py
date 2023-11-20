import wget
import tkinter as tk
from tkinter import filedialog
import os

def baixar_arquivo():
    link = entry_link.get()
    nome_arquivo = entry_nome_arquivo.get()
    pasta_salvar = filedialog.askdirectory()
    
    if link and nome_arquivo and pasta_salvar:
        caminho_completo = os.path.join(pasta_salvar, nome_arquivo)
        
        # Certifique-se de que o diretório de destino exista
        os.makedirs(pasta_salvar, exist_ok=True)
        
        wget.download(link, caminho_completo)
        resultado_label.config(text=f"Arquivo baixado com sucesso em:\n{caminho_completo}")
    else:
        resultado_label.config(text="Por favor, preencha todos os campos.")

# Configuração da interface
root = tk.Tk()
root.title("Baixar Arquivo")

# Entrada para o link
label_link = tk.Label(root, text="Link do arquivo:")
label_link.pack()
entry_link = tk.Entry(root, width=50)
entry_link.pack()

# Entrada para o nome do arquivo
label_nome_arquivo = tk.Label(root, text="Nome e extensão do arquivo:")
label_nome_arquivo.pack()
entry_nome_arquivo = tk.Entry(root, width=50)
entry_nome_arquivo.pack()

# Botão para baixar o arquivo
button_baixar = tk.Button(root, text="Baixar Arquivo", command=baixar_arquivo)
button_baixar.pack()

# Resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Iniciar a interface
root.mainloop()
