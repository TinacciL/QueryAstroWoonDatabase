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
C   3 B3 2 A3 1 D3
C   4 B4 3 A4 2 D4
H   4 B5 3 A5 2 D5
H   4 B6 3 A6 2 D6
H   5 B7 4 A7 3 D7
H   5 B8 4 A8 3 D8
H   5 B9 4 A9 3 D9
C   1 B10 2 A10 3 D10
H   1 B11 2 A11 3 D11
H   11 B12 1 A12 2 D12
H   11 B13 1 A13 2 D13
H   2 B14 1 A14 3 D14
H   3 B15 2 A15 1 D15
Variables:
B1        1.47711
B2        1.33947
A2      121.01978
B3        1.50452
A3      120.64987
D3      180.00113
B4        1.52533
A4      111.36610
D4      179.99604
B5        1.11160
A5      109.32098
D5       59.55136
B6        1.11160
A6      109.32132
D6      300.44248
B7        1.11111
A7      110.30012
D7      299.62430
B8        1.11041
A8      109.59473
D8      180.00068
B9        1.11111
A9      110.30082
D9       60.37614
B10        1.33495
A10      121.14041
D10      179.99557
B11        1.08673
A11      119.91480
D11      359.99622
B12        1.08522
A12      119.97242
D12      180.00051
B13        1.08606
A13      121.18971
D13      359.99992
B14        1.08765
A14      119.39836
D14      180.00117
B15        1.08794
A15      119.70274
D15        0.00007

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

