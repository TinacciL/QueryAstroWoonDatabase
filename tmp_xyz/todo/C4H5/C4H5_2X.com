%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq scf=xqc

 Title

0 2
C  
C   1 B1
C   2 B2 1 A2
H   1 B3 2 A3 3 D3
H   1 B4 2 A4 3 D4
C   3 B5 2 A5 1 D5
H   3 B6 2 A6 1 D6
H   6 B7 3 A7 2 D7
H   2 B8 1 A8 3 D8
Variables:
B1        1.33494
B2        2.43328
A2      149.37572
B3        1.08522
A3      119.97249
D3      180.00108
B4        1.08609
A4      121.17946
D4        0.00093
B5        1.33161
A5       31.56421
D5      359.99830
B6        1.08516
A6      152.10855
D6      359.99872
B7        1.08672
A7      119.40152
D7      179.99977
B8        1.08692
A8      119.07061
D8      179.99890

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P ROCCSD(T)/aug-cc-pvtz geom=allcheck guess=read

