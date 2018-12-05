#-*- coding:UTF-8 -*-

from tkinter import *

class novo:

    def __init__(self, janela):
        # Inicia como None
        self.jan = None
        self.caixa=Frame(janela)
        self.caixa.grid()
        self.b=Button(janela, text='Abrir', command=self.new_jan)
        self.b.grid()
        self.l1=Label(janela, text='raiz!')
        self.l1.grid()

    def new_jan(self):
        # Verifica se já foi criada
        if self.jan is None:
            self.jan=Tk()
            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_jan)
            self.l=Label(self.jan, text='apenas fechando essa janela poderá voltar ou clicar na raiz!')
            self.l.grid()
            self.jan.geometry('300x200')
        else:
            # Se já foi, basta colocá-la na frente
            self.jan.lift()

    def fecha_jan(self):
        # Seta de novo em None para recriar quando abrir
        self.jan.destroy()
        self.jan = None

root=Tk()

novo(root)
root.geometry('300x200')

root.mainloop()
novo()
