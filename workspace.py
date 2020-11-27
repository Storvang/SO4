from sympy import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

x, y, z, m, t = symbols("x y z m t")

init_printing(use_unicode=False, wrap_line=False)

class fysik:
    def __init__(self, s, fra, til):
        self.s = s
        self.fra = fra
        self.til = til

    def getVfunc(self):
        return lambdify(t, str(diff(s)))

    def streakning(self, v):
        s1 = lambdify(t, str(integral(v)))
        print(s1(slut) - s1(start))


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

            return [f, diffX, tf, intX, areal, self.start, self.slut]

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

    #[f, diffX, tf, intX, areal, self.start, self.slut]

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
    plot.plotDiff()
    plot.plotInt()
    plot.plotDiffFunc()
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
    plot.plotDiff()
    plot.plotInt()
    plot.plotDiffFunc()
    #print(functions)

elif antal == 0:
    s = lambdify(t, 60*t**3)
    fra = int(input("Start: "))
    til = int(input("Slut: "))
    fart = fysik(s, fra, til)
    v = fart.getVfunc()
    functions = [s, fra, til, v]
    print(fart.streakning(v))


#... osv
