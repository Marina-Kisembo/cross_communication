from tkinter import *

import decimal
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import *
from tkinter.ttk import *
import webview
import dataforweb as dw

import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
import webap as w
import numpy as np
# import FileDialog
import tkinter.filedialog as tkFileDialog
import cx_Oracle
from tkinter.ttk import Notebook
import pickle
import webbrowser
import pyautogui
import multiprocessing
import tkinter.font as tkFont
# from docx import *
import threading
import time
import queue
#
# from docx.shared import *


root = Tk()

tree = ttk.Treeview(root)

tree["columns"]=("one","two","three")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.column("three", width=100)
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("" , 0,  text="data1",  values=("3","4"))

tree.insert("", 1, text="data1",   values=("9","5"))

tree.insert("", 2, text="data1",   values=("4","10"))

tree.insert("", 3, text="data1",  values=("5","1"))

tree.insert("", 4, text="data2",   values=("9","0"))

tree.insert("", 5, text="data2",   values=("7","3"))

tree.insert("", 6, text="data2",  values=("1","2"))

tree.insert("", 7, text="data2",   values=("3","2"))


tree.pack()

B = Button(root, text ="Plot Web", command=lambda: w.start_server())
B.pack(padx=5, pady=5, expand=YES)
B.bind('<Return>', lambda event: w.start_server())

B.pack()
root.mainloop()