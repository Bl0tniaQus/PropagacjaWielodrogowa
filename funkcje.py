import math
import matplotlib.pyplot as plt
pi = math.pi

def modul_zesp(a,b):
	return math.sqrt((a * a) + (b * b))
def wykres(lista_d, lista_P):
    d0 = int(min(lista_d))
    dz = int(max(lista_d) + 1)
    plt.plot(lista_d, lista_P)
    plt.title("y = P(d) / P(d0)")
    plt.xlabel("d [m]")
    plt.ylabel(" P(d) / P(d0)")
    plt.xticks([d0 + n*300 for n in range((dz-d0)//300 + 1)])
    plt.grid()
    plt.show()
def dwa_wykresy(lista_d1, lista_P1, lista_d2, lista_P2):
    d0 = int(min(lista_d1))
    dz = int(max(lista_d1) + 1)
    plt.plot(lista_d1, lista_P1)
    plt.plot(lista_d2, lista_P2)
    plt.legend(['Jedna droga', 'Wiele dróg'])
    plt.title("y = P(d) / P(d0)")
    plt.xlabel("d [m]")
    plt.ylabel(" P(d) / P(d0)")
    plt.xticks([d0 + n*300 for n in range((dz-d0)//300 + 1)])
    plt.grid()
    plt.show()
def propagacja(f, PT, dz, d0, h1, h2, A1, A2, A3):
    dlugosc_fali = 299792458 / (f * 1e6)
    n = int(1 + (dz-d0)/(0.5 * dlugosc_fali))
    Ls = (dlugosc_fali / (4*pi * d0))**2
    krok = 0.5 * dlugosc_fali
    Pd0 = PT * Ls
    lista_d = []
    lista_P = []
    d = d0
    for i in range(n):
        d1 = math.sqrt((h1 - h2)**2 + d**2)
        d2 = math.sqrt((h1 + h2)**2 + d**2)
        d3 = math.sqrt((h1 - h2)**2 + (dz+(dz-d))**2)
        fi1 = (-2*pi * d1 / dlugosc_fali) % (2*pi)
        fi2 = (-2*pi * d2 / dlugosc_fali) % (2*pi)
        fi3 = (-2*pi * d3 / dlugosc_fali) % (2*pi)
        a1 = A1 *(1 / d1) * math.cos(fi1)
        b1 = A1 *(1 / d1) * math.sin(fi1)
        a2 = -A2 * (1 / d2) * math.cos(fi2)
        b2 = -A2 * (1 / d2) * math.sin(fi2)
        a3 = -A3 * (1 / d3) * math.cos(fi3)
        b3 = -A3 * (1 / d3) * math.sin(fi3)
        Pd = Pd0 * (d0**2) * (modul_zesp(a1+a2+a3, b1+b2+b3)**2)
        P = 10 * math.log10(Pd / Pd0)
        lista_d.append(d)
        lista_P.append(P)
        d = d + krok
    return lista_d, lista_P
	
