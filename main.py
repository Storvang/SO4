from sympy import *
import tkinter
import numpy as np
import matplotlib.pyplot as plt

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

    def drawWindow(self):
        pass

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


    #print(functions)
#... osv