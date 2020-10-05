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
C   6 B6 5 A6 4 D6
C   7 B7 6 A7 5 D7
C   8 B8 7 A8 6 D8
C   9 B9 8 A9 7 D9
H   1 B10 2 A10 3 D10
H   10 B11 9 A11 8 D11
Variables:
B1        1.20530
B2        1.41177
A2      180.00000
B3        1.20525
A3      180.00000
D3        0.00000
B4        1.41169
A4      180.00000
D4      360.00000
B5        1.20522
A5      180.00000
D5        0.00000
B6        1.41169
A6      180.00000
D6        0.00000
B7        1.20525
A7      180.00000
D7      360.00000
B8        1.41177
A8      180.00000
D8        0.00000
B9        1.20530
A9      180.00000
D9        0.00000
B10       1.05834
A10     180.00000
D10     360.00000
B11       1.05834
A11     180.00000
D11     360.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

