%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 1
C  
C   1 B1
C   2 B2 1 A2
C   3 B3 2 A3 1 D3
C   4 B4 3 A4 2 D4
C   5 B5 4 A5 3 D5
N   6 B6 5 A6 4 D6
C   1 B7 2 A7 3 D7
C   8 B8 1 A8 2 D8
C   9 B9 8 A9 1 D9
C   10 B10 9 A10 8 D10
Variables:
B1        1.28146
B2        1.28147
A2      179.97438
B3        1.28148
A3      179.97438
D3      360.00000
B4        1.28151
A4      179.97438
D4        0.00000
B5        1.28153
A5      179.97438
D5      360.00000
B6        1.25690
A6      179.97438
D6        0.00000
B7        1.28148
A7      179.97438
D7        0.00000
B8        1.28150
A8      179.97438
D8        0.00000
B9        1.28155
A9      179.97438
D9      360.00000
B10        1.30518
A10      179.97438
D10        0.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

