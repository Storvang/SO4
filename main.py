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
        def differentialregning():
            window = tk.Tk()
            window.title("SO4")

            frame_1 = tk.Frame(window, height=300, width=300, bg="yellow")

            a = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window, text="Intast funktion:")
            x_value_label = tk.Label(window, text="Intast x værdi:")
            tekst = tk.Label(window, text="noget tekst")
            funktion = tk.Entry(window)
            x_value = tk.Entry(window)
            btn1 = tk.Button(
                window,
                text="fuck me"
                )

            tekst.grid(column=1, row=0)
            funktion.grid(column=1, row=1)
            x_value.grid(column=1, row=2)
            btn1.grid(column=1, row=3)
            funktion_label.grid(column=0, row=1)
            x_value_label.grid(column=0, row=2)

            a.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window.mainloop()

        def integralregning():
            window1 = tk.Tk()
            window1.title("SO4")

            frame_1 = tk.Frame(window1, height=300, width=300, bg="yellow")

            a = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window1, text="Intast funktion:")
            x_value_label = tk.Label(window1, text="Intast x værdi:")
            tekst = tk.Label(window1, text="noget tekst")
            funktion = tk.Entry(window1)
            x_value = tk.Entry(window1)
            btn1 = tk.Button(
                window1,
                text="fuck me"
            )

            tekst.grid(column=1, row=0)
            funktion.grid(column=1, row=1)
            x_value.grid(column=1, row=2)
            btn1.grid(column=1, row=3)
            funktion_label.grid(column=0, row=1)
            x_value_label.grid(column=0, row=2)

            a.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window1.mainloop()

        def thorbjørns_hygge():


    def askingForVar(self):
        pass

window = window0(500, 500, 0, 0)
window.drawWindow()