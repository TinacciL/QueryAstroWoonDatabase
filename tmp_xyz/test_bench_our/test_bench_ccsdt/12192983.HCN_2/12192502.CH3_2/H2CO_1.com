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
O   1 B3 2 A3 3 D3
Variables:
B1        1.08442
B2        1.08442
A2      119.99994
B3        1.21945
A3      120.00003
D3      180.00012

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
