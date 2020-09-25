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
H   3 B5 2 A5 1 D5
C   4 B6 1 A6 2 D6
Variables:
B1        2.58682
B2        1.30519
A2      179.97438
B3        1.08442
A3      119.97900
D3      359.62601
B4        1.08442
A4      120.02122
D4      179.62151
B5        1.08443
A5      120.00507
D5        0.48573
B6        2.07235
A6       33.05840
D6      359.99988

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
