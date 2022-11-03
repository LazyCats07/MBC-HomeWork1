from tkinter import * 
import tkinter.font as font #untuk mengganti font
import math #Membuat sebuah pekerjaan matematika

root = Tk()
root.title("CALCULATOR")
root.geometry("310x400")
root["bg"] = "#d1d1d1"

myfont = font.Font(size=14) #untuk mengganti fontnya nanti 

e = Entry(root, width = 25,borderwith= 0)
e["font"] = myfont
e["bg"] = "#d1d1d1"
e.grid(row=0, column=0, columnspan=4, padx= 20, pady= 20)

# ----------------------------------------
# Note !!!
# Apa fungsi Tkinter?
# Tkinter menyediakan cara cepat dan mudah yang berorientasikan objek yang kuat dalam membuat aplikasi python berbasiskan GUI. Tkinter biasanya secara default di-bundle dengan Python. Jadi ketika kamu install Python, Tkinter juga akan ikut terinstal pula. Tkinter sebenarnya bentuk OOP dari TCL/TK.

# columspan = lebar sebanyak x kotak
# padx = padding x
# pady = padding y


