from sympy import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image


x, y, z, m = symbols("x y z m")

init_printing(use_unicode=False, wrap_line=False)
class fysik:
    def __init__(self, function, til, fra):
        self.function = function
        self.fra = fra
        self.til = til

    def getVfunc(self):
        return lambdify(t, str(diff(self.function)))

    def streakning(self):
        s1 = lambdify(t, self.function)
        return s1(self.fra) - s1(self.til)

class calculus:
    def __init__(self, funktion, start, slut, tangentPunkt):
        self.funktion = funktion
        self.start = start
        self.slut = slut
        self.tangentPunkt = tangentPunkt

    def function(self):

        f = lambdify(x, self.funktion)

        diffX = self.diffrantialregning(self.funktion)

        #print(diffX)

        tf = self.tangentFunction(f, diffX)
        intX = self.intergralregning(self.funktion)

        areal = intX(float(self.slut)) - intX(float(self.start))

        return [f, diffX, tf, intX, areal, self.start, self.slut]

    #[f, diffX, tf, intX, areal, self.start, self.slut]

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

    def plotDiff(self):

        # Idk
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax1 = fig.add_subplot()

        # Lim som er fra og til i x og y akserne
        plt.xlim((-10, 10))
        plt.ylim((-10, 10))

        # Hvad x og y akserne hedder
        plt.ylabel("$y$")
        plt.xlabel("$x$")

        # x og y akse i midten af koordinatsystemet
        left, right = ax.get_xlim()
        low, high = ax.get_ylim()
        plt.arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
        plt.arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

        # Firkanter :D !!!
        plt.grid(True)

        t1 = np.arange(-10.0, 10.0, 0.1)
        plt.plot(t1, self.functions[0](t1))
        plt.plot(t1, self.functions[2](t1))
        plt.show()

    def plotInt(self):

        # Idk
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax1 = fig.add_subplot()

        # Lim som er fra og til i x og y akserne
        plt.xlim((-10, 10))
        plt.ylim((-10, 10))

        # Hvad x og y akserne hedder
        plt.ylabel("$y$")
        plt.xlabel("$x$")

        # x og y akse i midten af koordinatsystemet
        left, right = ax.get_xlim()
        low, high = ax.get_ylim()
        plt.arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
        plt.arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

        # Firkanter :D !!!
        plt.grid(True)

        ix = np.linspace(float(self.functions[5]), float(self.functions[6]))
        iy = self.functions[0](ix)
        verts = [(self.functions[5], 0), *zip(ix, iy), (self.functions[6], 0)]
        poly = plt.Polygon(verts, facecolor="0.9", edgecolor="0.5")
        ax1.add_patch(poly)

        ax.set_xticks((float(self.functions[5]), float(self.functions[6])))
        ax.set_xticklabels((f"{float(self.functions[5])}", f"{float(self.functions[6])}"))
        ax.set_yticks([])

        t1 = np.arange(-10.0, 10.0, 0.1)
        plt.plot(t1, self.functions[0](t1))

        plt.show()

    def plotDiffFunc(self):
        # Idk
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax1 = fig.add_subplot()

        # Lim som er fra og til i x og y akserne
        plt.xlim((-10, 10))
        plt.ylim((-10, 10))

        # Hvad x og y akserne hedder
        plt.ylabel("$y$")
        plt.xlabel("$x$")

        # x og y akse i midten af koordinatsystemet
        left, right = ax.get_xlim()
        low, high = ax.get_ylim()
        plt.arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
        plt.arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

        # Firkanter :D !!!
        plt.grid(True)

        t1 = np.arange(-10.0, 10.0, 0.1)
        plt.plot(t1, functions[1](t1))
        plt.show()

    def fysikPlot(self):
        pass

class window0:
    def __init__(self, height, width, entry, label):
        self.height = height
        self.width = width
        self.entry = entry
        self.label = label
        self.funktioner = ["1 grads", "2 grads", "3 grads", "4 grads", "5 grads", "6 grads", "sinus", "cosinus", "tangent", "potens"]

    def drawWindow(self):
        def differentialregning(funktion):
            window = tk.Tk()
            window.title("SO4")

            frame_1 = tk.Frame(window, height=300, width=300)

            frame2_label = tk.Label(frame_1, text="Graf/frame 2")

            xval = StringVar()

            funktion_label = tk.Label(window, text="vælg funktion:")
            x_value_label = tk.Label(window, text="Intast x værdi:")
            tekst = tk.Label(window, text="differentialregning")
            x_value = tk.Entry(window, textvariable=xval)

            def beregn():
                x = xval.get()
                calc = calculus(funktion, 0, 0, int(x))
                veardier = calc.function()
                plotting = plot(veardier)
                plotting.plotDiff()



            btn1 = tk.Button(
                window,
                command=lambda: [beregn()],
                text="beregn"
                )

            quit_btn = tk.Button(
                window,
                command=lambda: [window.destroy(), drawmenu()],
                text="menu"
            )

            tekst.grid(column=1, row=0)
            x_value.grid(column=1, row=100)
            btn1.grid(column=1, row=101)
            quit_btn.grid(column=1, row=102)
            funktion_label.grid(column=0, row=1)
            x_value_label.grid(column=0, row=100)

            frame2_label.grid()
            frame_1.grid(column=3, row=1, rowspan=100)

            window.mainloop()

        def integralregning(funktion):
            window1 = tk.Tk()
            window1.title("SO4")

            aval = StringVar()
            bval = StringVar()

            frame_1 = tk.Frame(window1, height=300, width=300)

            frame2_label = tk.Label(frame_1, text="Graf/frame 2")

            def getVal():
                start = aval.get()
                slut = bval.get()
                calc = calculus(funktion, start, slut, 0)
                veadier = calc.function()
                print(veadier)
                plotting = plot(veadier)
                plotting.plotInt()


            a_value_label = tk.Label(window1, text="Intast a:")
            b_value_label = tk.Label(window1, text="Intast b:")
            tekst = tk.Label(window1, text="integralregning")
            a_value = tk.Entry(window1, textvariable=aval)
            b_value = tk.Entry(window1, textvariable=bval)
            btn1 = tk.Button(
                window1,
                command=lambda: [getVal()],
                text="beregn"
            )

            quit_btn = tk.Button(
                window1,
                command=lambda: [window1.destroy(), drawmenu()],
                text="menu"
            )

            variable = tk.StringVar(window1)
            variable.set("vælg funktion")

            tekst.grid(column=1, row=0)
            a_value.grid(column=1, row=2)
            b_value.grid(column=1, row=3)
            btn1.grid(column=1, row=4)
            quit_btn.grid(column=0, row=4)
            a_value_label.grid(column=0, row=2)
            b_value_label.grid(column=0, row=3)
            frame2_label.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window1.mainloop()

        #Fysik
        def thorbjørns_hygge():

            window2 = tk.Tk()
            window2.title("SO4")

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

            tekst.grid(column=1, row=0)
            funktion_box.grid(column=1, row=1)
            Hjem.grid(column=1, row=0)
            a_value.grid(column=1, row=2)
            btn1.grid(column=1, row=4)
            quit_btn.grid(column=0, row=4))
            a_value_label.grid(column=0, row=2)


            frame2_label.grid()
            frame_1.grid(column=2, row=0, rowspan=4)

            window2.mainloop()

        def drawmenu():
            FILENAME = 'Test2.png'
            root = tk.Tk()
            root.geometry("1222x569")
            root.configure(bg="white")
            canvas = tk.Canvas(root, width=2500, height=3000)
            canvas.place(x=0, y=0)

            funktion = StringVar()

            btn = tk.Entry(root, textvariable=funktion, bg="gray")
            btn.grid(column=3, row=3)

            tk_img = ImageTk.PhotoImage(file=FILENAME)
            canvas.create_image(611, 284.5, image=tk_img)
            quit_button = tk.Button(root, text="Differentialregning", anchor='w',
                                    command=lambda: [root.destroy(), differentialregning(funktion.get())],
                                    activebackground="#33B5E5")
            quit_button_window = canvas.create_window(570, 84.5, anchor='nw', window=quit_button)

            button = tk.Button(root, text="   Integralregning   ", anchor='w',
                               activebackground="#33B5E5", command=lambda: [root.destroy(), integralregning(funktion.get())])
            button_window = canvas.create_window(570, 134.5, anchor='nw', window=button)

            button1 = tk.Button(root, text=" Thorbjørns_hygge ", anchor='w',
                                activebackground="#33B5E5", command=lambda: [root.destroy(), thorbjørns_hygge()])
            button1_window = canvas.create_window(570, 184.5, anchor='nw', window=button1)

            # frame = tk.Frame(window, bg="white")



            # print(variable)
            skriv = tk.Label(root, text="Funktion:")
            skriv.grid(column=2, row=3)
            fill = tk.Label(root, bg="white", text="                                                                                                                                                                                 ")
            fill.grid(column=0, row=0)

            # add empty label in row 0 and column 0
           # l0 = tk.Label(root, bg='white', text='                                                                                                                                                                                            ')
            #l0.grid(column=2, row=2)
            #btn = tk.Button(root, anchor='w', activebackground="#33B5E5", text="vælg",
                      #      command=lambda: [check1(variable.get())])
            #btn_window = canvas.create_window(570, 234.5, anchor='nw', window=btn)

            root.mainloop()

        drawmenu()

    def askingForVar(self):
        pass

window = window0(500, 500, 0, 0)
window.drawWindow()