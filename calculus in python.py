from sympy import *
import pylab as lab
import numpy as np
import matplotlib.pyplot as plt


x, y, z, m = symbols("x y z m")

#O.o
init_printing(use_unicode=False, wrap_line=False)

#Funktion input
function = str(input("Intast funktion: "))

#Tangent input
tangetInput = float(input("Hvor ville du ser din tangent henne: "))

#Start intergral
start = float(input("Hvor ville du have intergralet til at starte: "))

#Slut intergral
slut = float(input("Hvor ville du have intergralet til at slutte: "))

#Funktion opstillet sådan python kan forstå det
#lamdify oversætter string til funktion
f = lambdify(x, function)

#Hældningkoeficient
df = lambdify(x, str(diff(function)))

#A-værdien
a = df(tangetInput)

print(f"Tagentens hælninger er {a}")

#B-værdien
"""
Vi bruger:
y = ax + b
Omkriver vi:
ax + b - y = 0
"""
#m = b vi bruger b som var navn
expr = a*tangetInput + m - f(tangetInput)

#Vi isolere b
b = solve(expr, m)

#punkt for tanget skærer
koordinat0 = [tangetInput, f(tangetInput)]

#Vi definere funktions forskrift for tangeten
g = lambdify(x, a*x + b[0])

#Printer funktionen
print(g(x))

#intergral af funktion til beregning af areal
Af = lambdify(x, str(integrate(function, x)))

#Arealet fra start til slut under kurven
areal = Af(slut) - Af(start)

#Fortæller arealet
print(f"Intergralet af funktionen: f(x) = {function} fra {start} til {slut} er {areal}")

t1 = np.arange(-10.0, 10.0, 0.1)

#Idk
fig = plt.figure()
ax = fig.add_subplot(111)

ax1 = fig.add_subplot()

#Lim som er fra og til i x og y akserne
plt.xlim((-10, 10))
plt.ylim((-10, 10))

#Hvad x og y akserne hedder
plt.ylabel("$y$")
plt.xlabel("$x$")

#x og y akse i midten af koordinatsystemet
left, right = ax.get_xlim()
low, high = ax.get_ylim()
plt.arrow(left, 0, right - left, 0, length_includes_head = True, head_width = 0.15)
plt. arrow(0, low, 0, high-low, length_includes_head = True, head_width = 0.15)

#Firkanter :D !!!
plt.grid(True)

#Intergral
ix = np.linspace(start, slut)
iy = f(ix)
verts = [(start, 0), *zip(ix, iy), (slut, 0)]
poly = plt.Polygon(verts, facecolor="0.9", edgecolor="0.5")
ax1.add_patch(poly)

#Plotter funktioner ind:
#Input funktionen
plt.plot(t1, f(t1))
#Tangent funktionen
plt.plot(t1, g(t1))

#Et punkt som er hvor tangenten skærer
plt.scatter(koordinat0[0], koordinat0[1])

#Viser grafen
plt.show()


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