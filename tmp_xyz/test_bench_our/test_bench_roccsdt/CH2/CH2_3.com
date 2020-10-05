%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 3
C  
H   1 B1
H   1 B2 2 A2
Variables:
B1        1.10940
B2        1.10940
A2      109.47000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P ROCCSD(T)/aug-cc-pvtz geom=allcheck guess=read
