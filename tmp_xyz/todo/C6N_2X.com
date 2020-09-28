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
N   5 B5 4 A5 3 D5
C   1 B6 2 A6 3 D6
Variables:
B1        1.28160
B2        1.28155
A2      179.97438
B3        1.28162
A3      179.97438
D3        0.00000
B4        1.22206
A4      175.60960
D4        0.00000
B5        1.15865
A5      179.10915
D5      180.00000
B6        1.30518
A6      179.97438
D6        0.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

