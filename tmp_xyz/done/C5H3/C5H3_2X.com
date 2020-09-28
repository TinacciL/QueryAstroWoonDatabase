%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 2
C  
C   1 B1
C   2 B2 1 A2
C   3 B3 2 A3 1 D3
C   4 B4 3 A4 2 D4
H   5 B5 4 A5 3 D5
H   1 B6 2 A6 3 D6
H   1 B7 2 A7 3 D7
Variables:
B1        1.46300
B2        1.20538
A2      179.97438
B3        1.41176
A3      179.97438
D3      347.18307
B4        1.20531
A4      179.97438
D4        7.09917
B5        1.05834
A5      179.97438
D5        1.53374
B6        1.10945
A6      109.48860
D6       79.52201
B7        1.10944
A7      109.50055
D7      199.55810

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

