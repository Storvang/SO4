from sympy import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

x, y, z, m = symbols("x y z m")

init_printing(use_unicode=False, wrap_line=False)

class calculus:
    def __init__(self, a, b, c, d, e, start, slut, tangentPunkt):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.start = start
        self.slut = slut
        self.tangentPunkt = tangentPunkt

    def function(self, antal):
        if antal == 1:
            function = str(self.a*x + self.b)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)

            return [f, diffX, tf, intX, areal]

        elif antal == 2:
            function = str(self.a*(x**2) + self.b*x + self.c)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)

            return [f, diffX, tf, intX, areal]

    def diffrantialregning(self, f):
        return lambdify(x, str(diff(f)))

    def tangentFunction(self, f, diffX):

        healdning = diffX(self.tangentPunkt)

        #print(healdning)

        expr = healdning*self.tangentPunkt + m - f(self.tangentPunkt)

        b1 = solve(expr, m)

        #print(b1)

        tf = lambdify(x, str(healdning*x + b1[0]))

        return tf

    def intergralregning(self, f):
        return lambdify(x, str(integrate(f, x)))

class plot:
    def __init__(self, functions):
        self.functions = functions


    def setup(self):
        plt.figure()

    def plot(self):
        pass


class window0:
    def __init__(self, height, width, entry, label):
        self.height = height
        self.width = width
        self.entry = entry
        self.label = label
        self.funktioner = ["1 grads", "2 grads", "3 grads", "4 grads", "5 grads", "6 grads", "sinus", "cosinus", "tangent", "potens"]

    def drawWindow(self):
        def differentialregning():
            window = tk.Tk()
            window.title("SO4")

            frame_1 = tk.Frame(window, height=300, width=300)

            frame2_label = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window, text="vælg funktion:")
            x_value_label = tk.Label(window, text="Intast x værdi:")
            tekst = tk.Label(window, text="differentialregning")
            x_value = tk.Entry(window)

            btn1 = tk.Button(
                window,
                text="beregn"
                )

            quit_btn = tk.Button(
                window,
                command=lambda: [window.destroy(), drawmenu()],
                text="menu"
            )

            def check(var):
                if var == "1 grads":
                    a_entry = tk.Entry(window)
                    a_label = tk.Label(window, text=x)
                    b_entry = tk.Entry(window)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)
                else:
                    pass

            variable = tk.StringVar(window)
            variable.set("vælg funktion")
            funktion_box = tk.OptionMenu(window, variable, *self.funktioner, command=lambda: [check(variable.get())])




            tekst.grid(column=1, row=0)
            funktion_box.grid(column=1, row=1)
            x_value.grid(column=1, row=100)
            btn1.grid(column=1, row=101)
            quit_btn.grid(column=1, row=102)
            funktion_label.grid(column=0, row=1)
            x_value_label.grid(column=1, row=103)

            frame2_label.grid()
            frame_1.grid(column=3, row=1, rowspan=100)

            window.mainloop()

        def integralregning():
            window1 = tk.Tk()
            window1.title("SO4")

            frame_1 = tk.Frame(window1, height=300, width=300)

            frame2_label = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window1, text="vælg funktion:")
            a_value_label = tk.Label(window1, text="Intast a:")
            b_value_label = tk.Label(window1, text="Intast b:")
            tekst = tk.Label(window1, text="integralregning")
            a_value = tk.Entry(window1)
            b_value = tk.Entry(window1)
            btn1 = tk.Button(
                window1,
                text="beregn"
            )

            quit_btn = tk.Button(
                window1,
                command=lambda: [window1.destroy(), drawmenu()],
                text="menu"
            )

            variable = tk.StringVar(window1)
            variable.set("vælg funktion")
            funktion_box = tk.OptionMenu(window1, variable, *self.funktioner)

            tekst.grid(column=1, row=0)
            funktion_box.grid(column=1, row=1)
            a_value.grid(column=1, row=2)
            b_value.grid(column=1, row=3)
            btn1.grid(column=1, row=4)
            quit_btn.grid(column=0, row=4)
            funktion_label.grid(column=0, row=1)
            a_value_label.grid(column=0, row=2)
            b_value_label.grid(column=0, row=3)

            frame2_label.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window1.mainloop()

        def thorbjørns_hygge():

            window2 = tk.Tk()
            window2.title("SO4")

            def hjem():
                window2.destroy()
                window0()

            frame_1 = tk.Frame(window2, height=300, width=300)

            frame2_label = tk.Label(frame_1, text="Graf/frame 2")

            funktion_label = tk.Label(window2, text="vælg funktion:")
            a_value_label = tk.Label(window2, text="Intast:")

            Hjem= tk.Button(window2, text="hjem", command=lambda: [window2.destroy(), drawmenu()])
            tekst = tk.Label(window2, text="Thorbjørns hygge program")

            a_value = tk.Entry(window2)

            btn1 = tk.Button(
                window2,
                text="beregn"
            )

            quit_btn = tk.Button(
                window2,
                command=lambda: [window2.destroy(), drawmenu()],
                text="menu"
            )

            variable = tk.StringVar(window2)
            variable.set("vælg funktion")
            funktion_box = tk.OptionMenu(window2, variable, *self.funktioner)

            tekst.grid(column=1, row=0)
            funktion_box.grid(column=1, row=1)
            Hjem.grid(column=1, row=0)
            #tekst.grid(column=1, row=0)
            a_value.grid(column=1, row=2)
            btn1.grid(column=1, row=4)
            quit_btn.grid(column=0, row=4)
            funktion_label.grid(column=0, row=1)
            a_value_label.grid(column=0, row=2)


            frame2_label.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window2.mainloop()

        def drawmenu():
            window = tk.Tk()
            window.title("menu")
            window.geometry("2500x3000")
            window.configure(bg='white')
            C = Canvas(window, bg="white", height=25, width=30)
            filename = PhotoImage(file="Test2.png")
            #image = Image.open(filename)

            #image = image.resize((800, 800), Image.ANTIALIAS) ## The (250, 250) is (height, width)

            background_label = Label(window, image=filename, bg="white")
            background_label.place(x=1, y=1, relwidth=1, relheight=1)



            def test():
                differentialregning()
                window.destroy()


            def bob():
                window.destroy()


            frame = tk.Frame(window, bg="white")
            btnbob = tk.Button(frame, text="Differentialregning", command=lambda: [window.destroy(),differentialregning()])
            btnpeter = tk.Button(frame, text="Integralregning", command= lambda: [window.destroy(),integralregning()])
            btnib = tk.Button(frame, text="Thorbjørns_hygge", command=lambda: [window.destroy(),thorbjørns_hygge()])
            #Hjembu=tk.Button(Text="Hjem", command=)


            btnbob.pack()
            btnpeter.pack()
            btnib.pack()
            frame.pack()
            window.mainloop()
            #C.pack()
        drawmenu()

    def askingForVar(self):
        pass

window = window0(500, 500, 0, 0)
window.drawWindow()

#Kommer ind i gui:
antal = int(input("Hvor mange kompunenter er det i funktion: "))

if antal == 1:
    a = int(input("Hvad er a værdien: "))
    b = int(input("Hvad er b værdien: "))
    start = float(input("Hvor skal integralet starte: "))
    slut = float(input("Hvor skal integralet slut: "))
    tangentPunkt = int(input("Hvor skal tangenten være: "))
    calc = calculus(a, b, 0, 0, 0, start, slut, tangentPunkt)
    functions = calc.function(antal)
    plot = plot(functions)
    plot.setup()

    #print(functions)

elif antal == 2:
    a = int(input("Hvad er a værdien: "))
    b = int(input("Hvad er b værdien: "))
    c = int(input("Hvad er c værdien: "))
    start = float(input("Hvor skal integralet starte: "))
    slut = float(input("Hvor skal integralet slut: "))
    tangentPunkt = int(input("Hvor skal tangenten være: "))
    calc = calculus(a, b, c, 0, 0, start, slut, tangentPunkt)
    functions = calc.function(antal)
    plot = plot(functions)
    plot.setup()


