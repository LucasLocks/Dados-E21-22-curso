#ex084.py
""" Crie um programa que mostra a data atual, formatada para
dia/mes/ano hora:minuto:segundo). (import datetime): faça um relógio que mostre
a hora atualizada por 15 segundos e interrompa. time.sleep (15) """

import time 
from datetime import datetime

for i in range(15):
    agora = datetime.now()
    agora = f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}'
    print (agora)
    time.sleep (1)

"""Código achei no google mostra um relógio na tela:
import tkinter as tk
import datetime
class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('Arial', 26), fg='Black')
        self.lblRelogio.pack(pady=30, padx=30)
        self.alteracao()
    def alteracao(self):
        now = datetime.datetime.now()
        self.lblRelogio['text'] = now.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)
janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop() """