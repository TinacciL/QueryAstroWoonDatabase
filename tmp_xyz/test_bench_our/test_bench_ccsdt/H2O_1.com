%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 1
O  
H   1 B1
H   1 B2 2 A2
Variables:
B1        0.99025
B2        0.99025
A2      104.51002

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
