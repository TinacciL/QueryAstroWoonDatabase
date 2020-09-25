%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 1
C  
H   1 B1
H   1 B2 2 A2
H   1 B3 2 A3 3 D3
C   1 B4 2 A4 3 D4
H   5 B5 1 A5 2 D5
C   5 B6 1 A6 2 D6
H   7 B7 5 A7 1 D7
C   7 B8 5 A8 1 D8
C   2 B9 1 A9 3 D9
H   2 B10 1 A10 3 D10
Variables:
B1        1.10207
B2        1.10207
A2      108.51389
B3        1.10044
A3      109.04547
D3      118.66302
B4        1.48051
A4      109.88918
D4      239.82290
B5        1.07140
A5      118.68101
D5       59.66967
B6        1.32290
A6      121.14125
D6      239.66967
B7        1.06310
A7      121.47520
D7        0.00001
B8        1.40275
A8      121.13081
D8      179.99987
B9        5.47349
A9       53.36732
D9      133.19620
B10        6.45513
A10       55.85868
D10      130.96318

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
