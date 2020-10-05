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
B1        4.95891
B2        1.37499
A2      163.01750
B3        2.57555
A3      162.98576
D3       -0.02458
B4        3.63789
A4      162.98974
D4       -0.02445
B5        1.09081
A5      101.78752 
D5     -124.39410
B6        1.09081
A6      101.78136
D6      124.38720
B7        1.20319
A7       17.30555
D7      180.00000
B8        1.08883
A8      128.29523
D8        0.00066
B9        1.52188
A9       17.08628
D9       -0.01439
B10       2.65911
A10      16.45400
D10    -180.00000
B11       1.09041
A11     110.44845
D11     121.07754
B12       1.09040
A12     110.44971
D12    -121.08700
B13       1.09298
A13     109.01089
D13    -122.29147
B14       1.09296
A14     109.00863
D14     121.73016

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

