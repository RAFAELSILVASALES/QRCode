
## import ###

from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import tkinter as tk
from typing import overload
from pyqrcode import create
import tkinter
import os
import validators
from tkinter import messagebox

### screen ##
tela = Tk()
tela.geometry("1208x498+11+110")
tela.minsize(120, 1)
tela.maxsize(1370, 749)
tela.resizable(0,  0)
tela.title("QR Code")
tela.configure(background="#d9d9d9")


### Canvas 1 ####


Canvas1 = tk.Canvas(tela)
Canvas1.place(relx=0.0, rely=0.0, relheight=1.096, relwidth=1.072)
Canvas1.configure(background="#8231cf")
Canvas1.configure(borderwidth="2")
Canvas1.configure(insertbackground="black")
Canvas1.configure(relief="ridge")
Canvas1.configure(selectbackground="blue")
Canvas1.configure(selectforeground="white")


### Canvas2  ###

Canvas2 = tk.Canvas(Canvas1)
Canvas2.place(relx=0.512, rely=0.0,
              relheight=0.919, relwidth=0.444)
Canvas2.configure(background="#FFFFFF")
Canvas2.configure(borderwidth="2")
Canvas2.configure(insertbackground="black")
Canvas2.configure(relief="ridge")
Canvas2.configure(selectbackground="blue")
Canvas2.configure(selectforeground="white")

###  TEXT QR CODE ###
Label3 = tk.Label(Canvas2)
Label3.place(relx=0.256, rely=0.074, height=47, width=251)
Label3.configure(background="#ffffff")
Label3.configure(disabledforeground="#a3a3a3")
Label3.configure(font="-family {Segoe UI} -size 20 -weight bold")
Label3.configure(foreground="#000000")
Label3.configure(text='''QR Code''')


### TEXT Insira Url ###

Label4 = tk.Label(Canvas2)
Label4.place(relx=0.043, rely=0.259, height=19, width=115)
Label4.configure(background="#ffffff")
Label4.configure(disabledforeground="#a3a3a3")
Label4.configure(font="-family {Segoe UI} -size 12 -weight bold")
Label4.configure(foreground="#000000")
Label4.configure(text='''Insira Url:''')

### TEXT ###

Label5 = tk.Label(Canvas2)
Label5.place(relx=0.043, rely=0.791, height=78, width=496)
Label5.configure(background="#ffffff")
Label5.configure(disabledforeground="#a3a3a3")
Label5.configure(font="-family {Segoe UI} -size 11 -weight bold")
Label5.configure(foreground="#000000")
Label5.configure(
    text='''Use este tipo de QR Code para abrir um link de qualquer página web .''')


### TEXT ###

Label6 = tk.Label(Canvas2)
Label6.place(relx=0.043, rely=0.300, height=78, width=496)
Label6.configure(background="#ffffff")
Label6.configure(disabledforeground="#a3a3a3")
Label6.configure(font="-family {Segoe UI} -size 11 -weight bold")
Label6.configure(foreground="#000000")
Label6.configure(
    text='''Use CTRL + V para inserir a URL desejável.''')


### CAMPO Entry ###

Entry1 = tk.Entry(Canvas2)
Entry1.place(relx=0.235, rely=0.259, height=20, relwidth=0.511)
Entry1.configure(background="#dcdcdc")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")

### FUNÇÃO para criar o qr_code e fazer a validação de url ###


def qr_code():
    global link
    link = Entry1.get()
    if not validators.url(link):
        messagebox.showwarning(
            "Aviso", "Atenção, para gerar o QR Code deve inserir uma URL válida.")

    if validators.url(link):
        link = create(link)
        link.png("QR_Code.png", scale=5)
        test = link.xbm(scale=5)
        global xbm_image
        xbm_image = tkinter.BitmapImage(
            data=test, background="white")
        image_view.config(image=xbm_image)


image_view = tk.Label(Canvas2)
image_view = tkinter.Label(tela)
image_view.place(relx=0.140, rely=0.200, height=300, width=300)
image_view.configure(background="#ffffff")
image_view.configure(disabledforeground="#a3a3a3")
image_view.configure(foreground="#000000")


### button ###

Button1 = tk.Button(Canvas2)
Button1.place(relx=0.278, rely=0.578, height=54, width=207)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#8231cf")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font="-family {Segoe UI} -size 14 -weight bold")
Button1.configure(foreground="#ffffff")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''QR Code''')
Button1.configure(command=qr_code)

### imagem ###
image = PhotoImage(file='arquivo\qr.png')

w = Label(tela, image=image)
w.configure(background="#ffffff")


w.place(x=790, y=30)

### canvas1 ###
Label1 = tk.Label(Canvas1)
Label1.place(relx=0.114, rely=0.051, height=75, width=348)
Label1.configure(background="#8231cf")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font="-family {Segoe UI} -size 20 -weight bold")
Label1.configure(foreground="#FFFFFF")
Label1.configure(text='''Gerador de QR Code''')


tela.mainloop()
