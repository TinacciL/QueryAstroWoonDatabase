%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 2
C  
O   1 B1
H   1 B2 2 A2
Variables:
B1        1.21945
B2        1.08442
A2      120.01111

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
