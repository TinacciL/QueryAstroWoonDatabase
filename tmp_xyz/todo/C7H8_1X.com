%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 1
C  
C   1 B1
C   2 B2 1 A2
C   2 B3 1 A3 3 D3
H   2 B4 1 A4 3 D4
H   1 B5 2 A5 3 D5
H   1 B6 2 A6 3 D6
C   2 B7 1 A7 3 D7
H   1 B8 2 A8 3 D8
C   1 B9 2 A9 3 D9
C   2 B10 1 A10 3 D10
H   10 B11 1 A11 2 D11
H   10 B12 1 A12 2 D12
H   11 B13 8 A13 2 D13
H   11 B14 8 A14 2 D14
Variables:
B1        4.96280
B2        1.41187
A2      164.96857
B3        2.61724
A3      165.19779
D3      359.92604
B4        3.67563
A4      165.36844
D4      359.86967
B5        1.11105
A5      101.36256
D5      235.62107
B6        1.11108
A6      101.21093
D6      123.27767
B7        1.20567
A7       15.87287
D7      180.25520
B8        1.11027
A8      126.79452
D8      359.53876
B9        1.52657
A9       17.07751
D9      359.20577
B10        2.67272
A10       16.49281
D10      180.26440
B11        1.11232
A11      108.82468
D11      120.52055
B12        1.11234
A12      108.86338
D12      238.89524
B13        1.11088
A13      108.55994
D13       59.14735
B14        1.11085
A14      108.49811
D14      300.92496

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

