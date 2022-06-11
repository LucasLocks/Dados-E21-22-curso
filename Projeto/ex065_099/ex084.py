#ex084.py
""" Crie um programa que mostra a data atual, formatada para
dia/mes/ano hora:minuto:segundo). (import datetime): faça um relógio que mostre
a hora atualizada por 15 segundos e interrompa. time.sleep (15) """

import time 
from datetime import datetime

a = 0
while a < 16:
    hj = datetime.now()
    hj = f'{hj.day}/{hj.month}/{hj.year} {hj.hour}:{hj.minute}:{hj.second}'
    print (hj)
    a = a + 1
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