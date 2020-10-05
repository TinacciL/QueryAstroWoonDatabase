%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq stable=opt

 Title

0 1
C  
C   1 B1
C   2 B2 1 A2
O   3 B3 2 A3 1 D3
Variables:
B1        1.28115
B2        1.28113
A2      180.00000
B3        1.19623
A3      180.00000
D3      360.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

