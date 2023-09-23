import tkinter as tk

janela = tk.Tk()
janela.title("Zeus")
janela.geometry("400x300")

rotulo = tk.Label(janela, text="Insira o Texto:")
rotulo.pack()

entrada = tk.Entry(janela, width=50)
entrada.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

def exibir_valor():
    valor_inserido = entrada.get()
    try:
        valor_convertido = float(valor_inserido)
        label_resultado.config(text=f"Valor inserido: {valor_convertido}")
    except ValueError:
        label_resultado.config(text="Insira um valor numérico válido.")

botao = tk.Button(janela, text="Exibir Valor", command=exibir_valor)
botao.pack()

janela.mainloop()
