# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:33:43 2020
Making some buttons for tic,tac,toe
@author: Aditya Ojha
"""
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.geometry("1000x1000")
e = tk.Entry(window,width = 50,fg="blue",borderwidth=5)
e.insert(0,"Enter your name")
e.pack()
def sayHello():
    msg = "Hello "+e.get()
    messagebox.showinfo(msg,msg)
    button2 = tk.Button(window,text="How are you today?")
    button2.pack()
def click():
    myLabel = tk.Label(window,text = e.get())
    myLabel.pack()
h = 25
w = 25
button = tk.Button(window,text = "Enter Your Name",command = sayHello,padx=h,pady=w)
button2 = tk.Button(window,text = "PRESSS MEEEEEE",command = click,bg="blue",fg="red")
button.pack()
button2.pack()
window.mainloop()