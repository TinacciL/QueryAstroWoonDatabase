%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 2
C  
C   1 B1
H   1 B2 2 A2
H   1 B3 2 A3 3 D3
C   2 B4 1 A4 3 D4
H   5 B5 2 A5 1 D5
H   2 B6 1 A6 3 D6
H   2 B7 1 A7 3 D7
H   5 B8 2 A8 1 D8
H   5 B9 2 A9 1 D9
Variables:
B1        1.52251
B2        1.11036
A2      109.92222
B3        1.11097
A3      110.55268
D3      120.36796
B4        1.52408
A4      110.82254
D4      178.81397
B5        1.11103
A5      110.25071
D5      300.04465
B6        1.11135
A6      109.45633
D6      299.73800
B7        1.11092
A7      109.00088
D7       58.66180
B8        1.11101
A8      110.37792
D8       60.77071
B9        1.11039
A9      109.58115
D9      180.39886

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

