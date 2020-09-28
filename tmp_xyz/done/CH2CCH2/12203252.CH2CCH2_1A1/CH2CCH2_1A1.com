%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 1
C  
C   1 B1
C   1 B2 2 A2
H   2 B3 1 A3 3 D3
H   2 B4 1 A4 3 D4
H   3 B5 1 A5 2 D5
H   3 B6 1 A6 2 D6
Variables:
B1        1.30524
B2        1.30528
A2      179.97438
B3        1.08441
A3      119.99019
D3      333.56837
B4        1.08442
A4      120.00803
D4      153.41365
B5        1.08441
A5      120.00299
D5      116.01349
B6        1.08440
A6      119.99343
D6      296.35979

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

