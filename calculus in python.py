from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x, y, z, m = symbols("x y z m")

init_printing(use_unicode=False, wrap_line=False)

#triFunc = ["cos", "sin", "tan"]

#Funktion input
function = str(input("Intast funktion: "))

#Tangent input
tangetInput = float(input("Hvor ville du ser din tangent henne: "))

#Funktion opstillet sådan python kan forstå det
f = lambdify(x, function)

#Hældningkoeficient
df = lambdify(x, str(diff(function)))

#A-værdien
a = df(tangetInput)

#B-værdien
expr = a*tangetInput + m - f(tangetInput)

b = solve(expr, m)

#punkt for tanget skærer
koordinat0 = [tangetInput, f(tangetInput)]

g = lambdify(x, a*x + b[0])

print(g(x))

#intergral af funktion til beregning af areal
Af = lambdify(x, str(integrate(function, x)))

t1 = np.arange(-10.0, 10.0, 0.1)

plt.xlim((-10, 10))

plt.plot(t1, f(t1))
plt.plot(t1, g(t1))
plt.scatter(koordinat0[0], koordinat0[1])
plt.show()
