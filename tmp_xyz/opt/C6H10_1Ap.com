%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 1
H  
H   1 B1
C   1 B2 2 A2
H   3 B3 1 A3 2 D3
C   4 B4 3 A4 1 D4
H   5 B5 4 A5 3 D5
C   6 B6 5 A6 4 D6
H   7 B7 6 A7 5 D7
C   8 B8 7 A8 6 D8
H   9 B9 8 A9 7 D9
H   10 B10 9 A10 8 D10
C   11 B11 10 A11 9 D11
H   12 B12 11 A12 10 D12
Variables:
B1        1.86924
B2        1.08522
A2       30.59574
B3        2.08975
A3       92.89886
D3      180.00000
B4        1.08675
A4       33.99271
D4      180.00000
B5        2.22083
A5      145.20957
D5      180.00000
B6        1.08734
A6       35.49115
D6      360.00000
B7        2.10673
A7      146.40087
D7      180.00000
B8        1.08674
A8       33.40067
D8        0.00000
B9        2.13959
A9      100.97357
D9      154.51878
B10        1.80731
A10       65.01703
D10       95.18361
B11        1.10973
A11       35.48162
D11       39.54432
B12        1.11120
A12      108.64925
D12      118.25982

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read
