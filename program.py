import funkcje
#DANE [zmieniane do każdego podpunktu]
#[MHz]
f = 1820
A1 = 0.8
A2 = 0.6
A3 = 0.4
#[m]
d0 = 200
dz = 3200
h1 = 50
h2 = 3
#[W]
PT = 500

d, p = funkcje.propagacja(f,PT,dz,d0,h1,h2,A1,0,0)
#funkcje.wykres(d, p)
d2, p2 = funkcje.propagacja(f,PT,dz,d0,h1,h2,A1,A2,A3)
funkcje.dwa_wykresy(d,p, d2, p2)
#zespol 2!!!
#L1 !!!
