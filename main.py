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



    def drawWindow():
        def differentialregning():
            window = tk.Tk()
            window.title("SO4")

            frame_1 = tk.Frame(window, height=300, width=300)

            a = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window, text="Intast funktion:")
            x_value_label = tk.Label(window, text="Intast x værdi:")
            tekst = tk.Label(window, text="differentialregning")
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

            frame_1 = tk.Frame(window1, height=300, width=300)

            a = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window1, text="Intast funktion:")
            a_value_label = tk.Label(window1, text="Intast a:")
            b_value_label = tk.Label(window1, text="Intast b:")
            tekst = tk.Label(window1, text="integralregning")
            funktion = tk.Entry(window1)
            a_value = tk.Entry(window1)
            b_value = tk.Entry(window1)
            btn1 = tk.Button(
                window1,
                text="fuck me"
            )

            tekst.grid(column=1, row=0)
            funktion.grid(column=1, row=1)
            a_value.grid(column=1, row=2)
            b_value.grid(column=1, row=3)
            btn1.grid(column=1, row=4)
            funktion_label.grid(column=0, row=1)
            a_value_label.grid(column=0, row=2)
            b_value_label.grid(column=0, row=3)

            a.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window1.mainloop()

        def thorbjørns_hygge():
            window2 = tk.Tk()
            window2.title("SO4")

            frame_1 = tk.Frame(window2, height=300, width=300)

            a = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window2, text="Intast funktion:")
            a_value_label = tk.Label(window2, text="Intast:")

            tekst = tk.Label(window2, text="Thorbjørns hygge program")
            funktion = tk.Entry(window2)
            a_value = tk.Entry(window2)

            btn1 = tk.Button(
                window2,
                text="fuck me"
            )

            tekst.grid(column=1, row=0)
            funktion.grid(column=1, row=1)
            a_value.grid(column=1, row=2)

            btn1.grid(column=1, row=4)
            funktion_label.grid(column=0, row=1)
            a_value_label.grid(column=0, row=2)


            a.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window2.mainloop()

        def drawmenu():
            window = tk.Tk()
            window.title("bob")

            frame = tk.Frame(window)
            btnbob = tk.Button(frame, text="Differentialregning", command=differentialregning)
            btnpeter = tk.Button(frame, text="Integralregning", command=integralregning)
            btnib = tk.Button(frame, text="Thorbjørns_hygge", command=thorbjørns_hygge)


            btnbob.grid()
            btnpeter.grid()
            btnib.grid()
            frame.grid()
            window.mainloop()
        drawmenu()
    drawWindow()
    def askingForVar(self):
        pass

window0()
#class menu:


 #   drawmenu()

#window = window0(500, 500, 0, 0)

#menu()