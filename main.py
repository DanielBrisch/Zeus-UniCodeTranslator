import tkinter as tk

janela = tk.Tk()
janela.title("Zeus")
janela.geometry("400x300")

rotulo = tk.Label(janela, text="Insira o Texto:")
rotulo.pack()

entrada = tk.Entry(janela, width=50)
entrada.pack()

    # try:
    #     valor_convertido = float(valor_inserido)
    #     label_resultado.config(text=f"Valor inserido: {valor_convertido}")
    # except ValueError:
    #     label_resultado.config(text="Insira um valor numérico válido.")

label_resultado = tk.Label(janela)
 
def exibir_valor():
    valor_inserido = entrada.get().strip() 
    if 'é' in valor_inserido:
        valor_modificado = valor_inserido.replace('é', '\\u00e1')
        label_resultado.config(text=f"Texto modificado: {valor_modificado}")
    else:
        label_resultado.config(text="Valor nao possui UniCode")

botao = tk.Button(janela, text="Exibir Valor", command=exibir_valor)
botao.pack(pady=20)

label_resultado.pack()

janela.mainloop()
