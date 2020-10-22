%nosave
%nproc=24
%mem=24gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq scf=xqc

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
C   9 B9 8 A9 1 D9
C   10 B10 9 A10 8 D10
Variables:
B1        1.32734
B2        1.22351
A2      180.00000
B3        1.34712
A3      180.00000
D3        0.00000
B4        1.21054
A4      180.00000
D4        0.00000
B5        1.36944
A5      180.00000
D5        0.00000
B6        1.15159
A6      180.00000
D6        0.00000
B7        1.24106
A7      180.00000
D7        0.00000
B8        1.30050
A8      180.00000
D8        0.00000
B9        1.27136
A9      180.00000
D9        0.00000
B10        1.2962
A10      180.0700
D10        0.0000

--Link1-- 
%nosave
%nproc=24
%mem=24gb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

