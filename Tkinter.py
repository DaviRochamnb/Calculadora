import tkinter as tk
from tkinter import *
from turtle import bgcolor, color, width
from Calculadora import *


class CalculadoraIp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora de Redes")
        self.janela.configure(bg='gray')
        self.janela.geometry('570x600')
        self.janela.resizable(width = False, height = False)

        label_ip = Label(janela, text="IP:", background='white') 
        label_ip.grid(row=0, column=0, padx=3, pady=3)
        self.entry1 = Entry(janela, width=40)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        label_mask = Label(janela, text="Máscara:", background='white')
        label_mask.grid(row=1, column=0, padx=10, pady=10)
        self.entry2 = Entry(janela, width=40)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        button_calcular = Button(janela, text="Calcular", command=self.executar, width=30, bg='black', fg='white')
        button_calcular.grid(row=2, column=0, pady=20)
        self.resultado_text = tk.Text(janela, height=20, width=68, bg='#d9d9d9')
        self.resultado_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def executar(self):
        valor_ip = self.entry1.get()
        valor_mask = self.entry2.get()
        ip = Ip() 
        ip.set_ip(valor_ip.split('.'), base=10)
        ip.set_mask(valor_mask.split('.'), base=10)
        ip.set_end_rede()
        ip.set_end_bcast()

        self.resultado_text.delete('1.0', tk.END)
        self.resultado_text.insert(tk.END, f"IP: {ip.get_ip(base=10)}\n")
        self.resultado_text.insert(tk.END, f"Máscara: {ip.get_mask(base=10)}\n")
        self.resultado_text.insert(tk.END, f"Rede: {ip.get_rede(base=10)}\n")
        self.resultado_text.insert(tk.END, f"Broadcast: {ip.get_bcast(base=10)}\n")
        self.resultado_text.insert(tk.END, f"Total de hosts: {ip.get_qtd_hosts()}\n" )



if __name__ == "__main__":
    janela = tk.Tk()
    app = CalculadoraIp(janela)
    janela.mainloop()



