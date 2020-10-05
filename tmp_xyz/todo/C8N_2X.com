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
C   5 B5 4 A5 3 D5
N   6 B6 5 A6 4 D6
C   1 B7 2 A7 3 D7
C   8 B8 1 A8 2 D8
Variables:
B1        1.28099
B2        1.28098
A2      179.97438
B3        1.28088
A3      179.97438
D3      359.99987
B4        1.28110
A4      179.97438
D4      359.99988
B5        1.28110
A5      179.97438
D5      359.99991
B6        1.25683
A6      179.97438
D6      359.99994
B7        1.28121
A7      179.97438
D7      359.99986
B8        1.30497
A8      179.97438
D8      359.99988

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

