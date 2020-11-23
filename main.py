from sympy import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

class calculus:
    def __init__(self, a, b, c, d, e, start, slut):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.start = start
        self.slut = slut

    def function(self):
        pass

    def diffrantialregning(self):
        pass

    def intergralregning(self):
        pass

    def tangentFunction(self):
        pass

class plot:
    def __init__(self, function, diffX, intX):
        self.function = function
        self.diffX = diffX
        self.intX = intX

    def setup(self):
        pass

    def plot(self):
        pass


class window0:
    def __init__(self, height, width, entry, label):
        self.height = height
        self.width = width
        self.entry = entry
        self.label = label


    def drawWindow(self):
        window = tk.Tk()
        window.title("SO4")

        frame_1 = tk.Frame(window, height=300, width=300)
        frame_2 = tk.Frame(frame_1, height=300, width=300)

        frame_1.grid()
        frame_2.grid(column=1)

        a = tk.Label(frame_2, text="Frame 2")
        a.pack()

        tekst = tk.Label(frame_1, text="noget tekst")
        funktion = tk.Entry(frame_1)
        x_value = tk.Entry(frame_1)
        btn1 = tk.Button(
            frame_1
            text="fuck me"
            )

        tekst.grid(column=0)
        funktion.grid(column=0)
        x_value.grid(column=0)
        btn1.grid(column=0)

        window.mainloop()

    def askingForVar(self):
        pass

window = window0(500, 500, 0, 0)
window.drawWindow()