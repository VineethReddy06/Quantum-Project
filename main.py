import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL
import warnings
import numpy as np
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

warnings.simplefilter("ignore")
root=tkinter.TK()
root.title('Quantum Glasses')
root.iconbitmap(default='logo.ico')
root.geometry('399x410')
root.resizable(0,0)
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial',18)
display_font = ('Arial',32)
