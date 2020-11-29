from sympy import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image


x, y, z, m = symbols("x y z m")

init_printing(use_unicode=False, wrap_line=False)

class calculus:
    def __init__(self, a, b, c, d, e, f, g, start, slut, tangentPunkt, typeFunc):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.start = start
        self.slut = slut
        self.tangentPunkt = tangentPunkt
        self.typeFunc = typeFunc

    def function(self, antal):
        #1 grads
        if antal == 1:
            function = str(self.a*x + self.b)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)

            return [f, diffX, tf, intX, areal]
        #2 grads
        elif antal == 2:
            function = str(self.a*(x**2) + self.b*x + self.c)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #3 grads
        elif antal == 3:
            function = str(self.a*(x**3) + self.b*(x**2) + self.c*x + self.d)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #4 grads
        elif antal == 4:
            function = str(self.a*(x**4) + self.b*(x**3) + self.c*(x**2) + self.d*x + self.e)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #5 grads
        elif antal == 5:
            function = str(self.a*(x**5) + self.b*(x**4) + self.c*(x**3) + self.d*(x**2) + self.e*x + self.f)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #6 grads
        elif antal == 6:
            function = str(self.a*(x**6) + self.b*(x**5) + self.c*(x**4) + self.d*(x**3) + self.e*(x**2) + self.f*x + self.g)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #cos
        elif antal == 7:
            function = str(cos(self.a*x))
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #sin
        elif antal == 8:
            function = str(sin(self.a*x))
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #tan
        elif antal == 9:
            function = str(tan(self.a*x))
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]

        #potens
        elif antal == 10:
            function = str(self.b*self.a**x)
            f = lambdify(x, function)
            diffX = self.diffrantialregning(function)

            #print(diffX)

            tf = self.tangentFunction(f, diffX)
            intX = self.intergralregning(function)

            areal = intX(self.slut) - intX(self.start)
            return [f, diffX, tf, intX, areal]
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
        plt.plot(t1, functions[0](t1))
        plt.plot(t1, functions[2](t1))
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

        ix = np.linspace(functions[5], functions[6])
        iy = functions[0](ix)
        verts = [(functions[5], 0), *zip(ix, iy), (functions[6], 0)]
        poly = plt.Polygon(verts, facecolor="0.9", edgecolor="0.5")
        ax1.add_patch(poly)

        t1 = np.arange(-10.0, 10.0, 0.1)
        plt.plot(t1, functions[0](t1))

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






            tekst.grid(column=1, row=0)
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
            a_value.grid(column=1, row=2)
            btn1.grid(column=1, row=4)
            quit_btn.grid(column=0, row=4)
            funktion_label.grid(column=0, row=1)
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
            tk_img = ImageTk.PhotoImage(file=FILENAME)
            canvas.create_image(611, 284.5, image=tk_img)
            quit_button = tk.Button(root, text="Differentialregning", anchor='w',
                                    command=lambda: [root.destroy(), differentialregning()],
                                    activebackground="#33B5E5")
            quit_button_window = canvas.create_window(570, 84.5, anchor='nw', window=quit_button)

            button = tk.Button(root, text="   Integralregning   ", anchor='w',
                               activebackground="#33B5E5", command=lambda: [root.destroy(), integralregning()])
            button_window = canvas.create_window(570, 134.5, anchor='nw', window=button)

            button1 = tk.Button(root, text=" Thorbjørns_hygge ", anchor='w',
                                activebackground="#33B5E5", command=lambda: [root.destroy(), thorbjørns_hygge()])
            button1_window = canvas.create_window(570, 184.5, anchor='nw', window=button1)

            # frame = tk.Frame(window, bg="white")
            def check1(var):
                master = root
                print(var)
                if var == self.funktioner[0]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x")
                    b_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)


                elif var == self.funktioner[1]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x^2")
                    b_entry = tk.Entry(master=root)
                    b_label = tk.Label(master=root, text="x")
                    c_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)
                    b_label.grid(column=1, row=3, sticky=tk.W)
                    c_entry.grid(column=0, row=4, sticky=tk.E)

                elif var == self.funktioner[2]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x^3")
                    b_entry = tk.Entry(master=root)
                    b_label = tk.Label(master=root, text="x^2")
                    c_entry = tk.Entry(master=root)
                    c_label = tk.Label(master=root, text="x")
                    d_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)
                    b_label.grid(column=1, row=3, sticky=tk.W)
                    c_entry.grid(column=0, row=4, sticky=tk.E)
                    c_label.grid(column=1, row=4, sticky=tk.W)
                    d_entry.grid(column=0, row=5, sticky=tk.E)

                elif var == self.funktioner[3]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x^4")
                    b_entry = tk.Entry(master=root)
                    b_label = tk.Label(master=root, text="x^3")
                    c_entry = tk.Entry(master=root)
                    c_label = tk.Label(master=root, text="x^2master=root")
                    d_entry = tk.Entry(master=root)
                    d_label = tk.Label(master=root, text="x")
                    e_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)
                    b_label.grid(column=1, row=3, sticky=tk.W)
                    c_entry.grid(column=0, row=4, sticky=tk.E)
                    c_label.grid(column=1, row=4, sticky=tk.W)
                    d_entry.grid(column=0, row=5, sticky=tk.E)
                    d_label.grid(column=1, row=5, sticky=tk.W)
                    e_entry.grid(column=0, row=6, sticky=tk.E)

                elif var == self.funktioner[4]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x^5")
                    b_entry = tk.Entry(master=root)
                    b_label = tk.Label(master=root, text="x^4")
                    c_entry = tk.Entry(master=root)
                    c_label = tk.Label(master=root, text="x^3")
                    d_entry = tk.Entry(master=root)
                    d_label = tk.Label(master=root, text="x^2")
                    e_entry = tk.Entry(master=root)
                    e_label = tk.Label(master=root, text="x")
                    f_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)
                    b_label.grid(column=1, row=3, sticky=tk.W)
                    c_entry.grid(column=0, row=4, sticky=tk.E)
                    c_label.grid(column=1, row=4, sticky=tk.W)
                    d_entry.grid(column=0, row=5, sticky=tk.E)
                    d_label.grid(column=1, row=5, sticky=tk.W)
                    e_entry.grid(column=0, row=6, sticky=tk.E)
                    e_label.grid(column=1, row=6, sticky=tk.W)
                    f_entry.grid(column=0, row=7, sticky=tk.E)

                elif var == self.funktioner[5]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x^6")
                    b_entry = tk.Entry(master=root)
                    b_label = tk.Label(master=root, text="x^5")
                    c_entry = tk.Entry(master=root)
                    c_label = tk.Label(master=root, text="x^4")
                    d_entry = tk.Entry(master=root)
                    d_label = tk.Label(master=root, text="x^3")
                    e_entry = tk.Entry(master=root)
                    e_label = tk.Label(master=root, text="x^2")
                    f_entry = tk.Entry(master=root)
                    f_label = tk.Label(master=root, text="x")
                    g_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)
                    b_label.grid(column=1, row=3, sticky=tk.W)
                    c_entry.grid(column=0, row=4, sticky=tk.E)
                    c_label.grid(column=1, row=4, sticky=tk.W)
                    d_entry.grid(column=0, row=5, sticky=tk.E)
                    d_label.grid(column=1, row=5, sticky=tk.W)
                    e_entry.grid(column=0, row=6, sticky=tk.E)
                    e_label.grid(column=1, row=6, sticky=tk.W)
                    f_entry.grid(column=0, row=7, sticky=tk.E)
                    f_label.grid(column=1, row=7, sticky=tk.W)
                    g_entry.grid(column=0, row=8, sticky=tk.E)

                elif var == self.funktioner[6]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x")
                    b_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)

                elif var == self.funktioner[7]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x")
                    b_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)

                elif var == self.funktioner[8]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="x")
                    b_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)

                elif var == self.funktioner[9]:
                    a_entry = tk.Entry(master=root)
                    a_label = tk.Label(master=root, text="^x")
                    b_entry = tk.Entry(master=root)

                    a_entry.grid(column=0, row=2, sticky=tk.E)
                    a_label.grid(column=1, row=2, sticky=tk.W)
                    b_entry.grid(column=0, row=3, sticky=tk.E)

                else:
                    pass

            variable = tk.StringVar(root)
            variable.set("vælg funktion")
            # print(variable)
            funktionbox = tk.OptionMenu(root, variable, *self.funktioner)
            funktionbox.grid()
            btn= tk.Button(root, text='vælg', command= lambda: [check1(variable.get())])
            btn.grid()
            #btn = tk.Button(root, anchor='w', activebackground="#33B5E5", text="vælg",
                      #      command=lambda: [check1(variable.get())])
            #btn_window = canvas.create_window(570, 234.5, anchor='nw', window=btn)

            root.mainloop()

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







    variable = tk.StringVar(window)
    variable.set("vælg funktion")
    # print(variable)
    funktion_box = tk.OptionMenu(window, variable, *self.funktioner)
    btn = tk.Button(window, text="vælg", command=lambda: check1(variable.get()))
    btn.grid()