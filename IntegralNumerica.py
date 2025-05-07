from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

Funcion = input("Ingresa la funcion: ")
A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))
C = (A + B) / 2

Sustitucion1 = Funcion.replace("x", str(A))
Sustitucion1 = Sustitucion1.replace("^", "**")

Sustitucion2 = Funcion.replace("x", str(B))
Sustitucion2 = Sustitucion2.replace("^", "**")

Sustitucion3 = Funcion.replace("x", str(C))
Sustitucion3 = Sustitucion3.replace("^", "**")

FA = eval(Sustitucion1)
FB = eval(Sustitucion2)
FC = eval(Sustitucion3)

print("F(", A ,") =", FA)
print("F(", B, ") =", FB)
print("F(", C, ") =", FC)

I = (B - A) * ((FA + FB + 4 * FC) / 6)

print("I =",I)



x = np.linspace(A, B, 100)

func_plot = Funcion.replace("^", "**")
y = [eval(func_plot, {"x": val, "np": np}) for val in x]

plt.plot(x, y)
plt.fill_between(x, y, alpha=0.3, color='blue')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title("Prueba")
#plt.savefig('grafica_lineal.png')
plt.show()