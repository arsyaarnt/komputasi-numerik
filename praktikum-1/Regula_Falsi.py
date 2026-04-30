import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

f_x = input("f(x): ")
a = float(input("Batas bawah (a): "))
b = float(input("Batas atas (b): "))
d = int(input("Ketelitian: "))

x = symbols('x')
f_sym = sympify(f_x)
f = lambdify(x, f_sym, 'numpy')

tol = 0.5 * 10**(-d)

if f(a) * f(b) > 0:
    print("Akar tidak ditemukan.\n")
    exit()

print("\nIterasi:")
print(f"{'i':>3} | {'a':>12} | {'b':>12} | {'c':>12} | {'f(a)':>12} | {'f(b)':>12} | {'f(c)':>12}")

i = 1
while True:
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    fa = f(a)
    fb = f(b)
    fc = f(c)

    print(f"{i:>3} | {a:>12.{d}f} | {b:>12.{d}f} | {c:>12.{d}f} | {fa:>12.{d}f} | {fb:>12.{d}f} | {fc:>12.{d}f}")

    if abs(fc) < tol or abs(b - a) < tol:
        break

    if fa * fc < 0:
        b = c
    else:
        a = c
    
    i += 1

print("\nAkar: ")
print(f"x = {c:.{d}f}")

x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = f(x_vals)

plt.axhline(0)
plt.axvline(0)
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(c, f(c), label="Akar", color='red')

plt.title("Metode Regula Falsi")
plt.legend()
plt.grid()
plt.show()
