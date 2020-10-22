%nosave
%nproc=24
%mem=8gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq scf=xqc

 Title

0 1
C  
C   1 B1
C   2 B2 1 A2
C   3 B3 2 A3 1 D3
C   4 B4 3 A4 2 D4
C   5 B5 4 A5 3 D5
O   6 B6 5 A6 4 D6
C   1 B7 2 A7 3 D7
Variables:
B1        1.28116
B2        1.28110
A2      179.97438
B3        1.28097
A3      179.97438
D3        0.00000
B4        1.28115
A4      179.97438
D4        0.00000
B5        1.28113
A5      179.97438
D5        0.00000
B6        1.19623
A6      179.97438
D6      360.00000
B7        1.30499
A7      179.97438
D7        0.00000

--Link1-- 
%nosave
%nproc=24
%mem=8gb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

