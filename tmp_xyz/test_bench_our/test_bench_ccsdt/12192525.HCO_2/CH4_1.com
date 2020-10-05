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
H   1 B4 2 A4 3 D4
Variables:
B1        1.10940
B2        1.10940
A2      109.47121
B3        1.10940
A3      109.47122
D3      240.00000
B4        1.10940
A4      109.47123
D4      120.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
