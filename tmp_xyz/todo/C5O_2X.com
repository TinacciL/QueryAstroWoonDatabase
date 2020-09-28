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
O   5 B5 4 A5 3 D5
Variables:
B1        1.30519
B2        1.28158
A2      179.97438
B3        1.28154
A3      179.97438
D3        0.00000
B4        1.28156
A4      179.97438
D4      360.00000
B5        1.19625
A5      179.97438
D5        0.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

