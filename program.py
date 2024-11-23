import funkcje
#[MHz]
f = 5

A1 = 0.8
A2 = 0.7
A3 = 0.4
#[m]
d0 = 1000
dz = 5000
h1 = 50
h2 = 3

#[W]
PT = 500

funkcje.propagacja_2_drogowa(f,PT,dz,d0,h1,h2,A1,A2)
funkcje.propagacja_3_drogowa(f,PT,dz,d0,h1,h2,A1,A2,A3)
