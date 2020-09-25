%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt optcyc=120 freq

 Title

0 2
C  
C   1 B1
C   2 B2 1 A2
H   1 B3 2 A3 3 D3
H   1 B4 2 A4 3 D4
H   2 B5 1 A5 3 D5
C   1 B6 2 A6 3 D6
Variables:
B1        2.41585
B2        1.20558
A2      151.87972
B3        1.08644
A3       90.50801
D3        0.00000
B4        1.08435
A4      150.27912
D4      180.00000
B5        2.26389
A5      151.87752
D5        0.00000
B6        1.33238
A6       30.69985
D6      180.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
