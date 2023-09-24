import sys
import tkinter as tk
import os

if sys.platform == 'win32':
    import ctypes
    my_app_id = 'myappid' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)


janela = tk.Tk()
janela.title("Zeus")
janela.geometry("400x160")
janela.configure(bg="black")

icone_path = os.path.abspath('img/raiop.ico')
janela.iconbitmap(icone_path)
janela.wm_iconbitmap(icone_path)

fonte_comic_sans = ("Comic Sans MS", 14)
rotulo = tk.Label(janela, font=fonte_comic_sans, text="Insira o Texto", fg="white", bg="black")
rotulo.pack()

entrada = tk.Entry(janela, width=50)
entrada.pack()

label_resultado = tk.Label(janela)
 
def exibir_valor():
    valor_inserido = entrada.get().strip() 
    valor_modificado = valor_inserido

    for caractere, substituicao in [('é', '\\u00e1'), ('É', '\\u00c9'), ('á', '\\u00E1'),
                                ('Á', '\\u00C1'), ('Ó','\\u00D3'), ('ó','\\u00F3'),
                                ('í','\\u00ED'), ('Í','\\u00CD'), ('ú','\\u00FA'),
                                ('Ú','\\u00DA'), ('ã','\\u00E3'), ('Ã','\\u00C3'),
                                ('õ','\\u00F5'), ('Õ','\\u00D5'), ('ñ','\\u00F1'),
                                ('Ñ','\\u00D1'), ('â','\\u00E2'), ('Â','\\u00C2'),
                                ('ê','\\u00EA'), ('Ê','\\u00CA'), ('ô','\\u00F4'),
                                ('Ô','\\u00D4'), ('û','\\u00FB'), ('Û','\\u00DB'),
                                ('ç', '\\u00E7'), ('Ç', '\\u00C7')]:
        if caractere in valor_inserido:
            valor_modificado = valor_modificado.replace(caractere, substituicao)

    resultado_entry.config(state='normal') 
    resultado_entry.delete(0, tk.END)  
    resultado_entry.insert(0, valor_modificado)
    resultado_entry.config(state='readonly')
    

botao = tk.Button(janela, text="Exibir Valor", command=exibir_valor, borderwidth=4)
botao.pack(pady=20)

resultado_entry = tk.Entry(janela, state='readonly', width=50)
resultado_entry.pack()

janela.mainloop()
