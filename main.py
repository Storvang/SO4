from sympy import *
import tkinter
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
        self.funcion = function
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
        pass

    def askingForVar(self):
        pass

