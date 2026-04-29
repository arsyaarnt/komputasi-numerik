# Praktikum 1 - Regula Falsi
## Kelompok 10

|     NRP    |         Nama        |
|:----------:|:-------------------:|
| 5025251022 | Ahmad Radho Alfariz |
| 5025251047 | Akhmad Fahmi        |
| 5025251059 | Arsya Argananta     |

## Penjelasan dan Potongan Kode
#### 1. Mengimport library yang diperlukan untuk kebutuhan perhitungan numerik.
```python
import numpy as np #untuk pengolahan angka / array
import matplotlib.pyplot as plt #untuk visualisasi grafik
from sympy import symbols, sympify, lambdify #manipulasi simbolik untuk membaca input fungsi
```
#### 2. Input data yang dibutuhkan.
```python
f_x = input("f(x): ")
a = float(input("Batas bawah (a): "))
b = float(input("Batas atas (b): "))
d = int(input("Ketelitian: "))
```
#### 3. Mengonversi input string fungsi agar dipahami oleh python.
```python
x = symbols('x')
f_sym = sympify(f_x)
f = lambdify(x, f_sym, 'numpy')
tol = 0.5 * 10**(-d) #menentukan batas toleransi
```
#### 4. Sebagai langkah preventif karena dalam metode regula falsi, syaratnya adalah nilai f(a) dan f(b) harus memiliki tanda yang berbeda (satu positif dan satu negatif). 
```python
if f(a) * f(b) > 0:
    exit()
```
#### 5. Menampilkan judul dan kolom tabel iterasi.
```pyhton
print("\nIterasi:")
print(f"{'i':>3} | {'a':>12} | {'b':>12} | {'c':>12} | {'f(a)':>12} | {'f(b)':>12} | {'f(c)':>12}")
``` 
#### 6. Perhitungan regula falsi.
```python
c  = (a * f(b) - b * f(a)) / (f(b) - f(a))
fa = f(a)
fb = f(b)
fc = f(c)
```
#### 7. Output dari perhitungan setiap iterasi.
```python
print(f"{i:>3} | {a:>12.{d}f} | {b:>12.{d}f} | {c:>12.{d}f} | {fa:>12.{d}f} | {fb:>12.{d}f} | {fc:>12.{d}f}")
```
#### 8. Kondisi berhenti dan pembaruan interval.
```python
if abs(fc) < tol or abs(b - a) < tol:
    break

if fa * fc < 0:
    b = c
else:
    a = c
```
#### 9. Output nilai akar.
```python
print("\nAkar: ")
print(f"x = {c:.{d}f}")
```
#### 10. Membuat data kurva.
```python
x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = f(x_vals)
```
#### 11. Memasukkan elemen-element plot yang dibutuhkan.
```python
plt.axhline(0) #sumbu x
plt.axvline(0) #sumbu y
plt.plot(x_vals, y_vals, label="f(x)") #menggambar kurva secara kontinu
plt.scatter(c, f(c), label="Akar", color='red') #membuat titik
```
#### 12. Dekorasi plot.
```python
plt.title("Metode Regula Falsi") #judul
plt.legend() #menampilkan label 
plt.grid() #garis bantu (grid)
plt.show() #menampilkan plot ke layar
```

## Full Code
```python
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
```


