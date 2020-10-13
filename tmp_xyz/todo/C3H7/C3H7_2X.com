%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq scf=xqc

 Title

0 2
C  
C   1 B1
C   1 B2 2 A2
H   2 B3 1 A3 3 D3
H   2 B4 1 A4 3 D4
H   3 B5 1 A5 2 D5
H   3 B6 1 A6 2 D6
H   3 B7 1 A7 2 D7
H   1 B8 2 A8 3 D8
H   1 B9 2 A9 3 D9
Variables:
B1        1.52251
B2        1.52408
A2      110.82255
B3        1.11036
A3      109.92224
D3      181.18654
B4        1.11097
A4      110.55259
D4       60.81867
B5        1.11039
A5      109.58114
D5      179.60148
B6        1.11101
A6      110.37798
D6      299.22966
B7        1.11103
A7      110.25068
D7       59.95574
B8        1.11092
A8      109.00091
D8      120.15213
B9        1.11135
A9      109.45627
D9      239.07593

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P ROCCSD(T)/aug-cc-pvtz geom=allcheck guess=read

