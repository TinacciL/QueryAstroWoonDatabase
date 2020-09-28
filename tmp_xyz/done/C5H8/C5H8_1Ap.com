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
H   1 B5 2 A5 3 D5
H   1 B6 2 A6 3 D6
H   2 B7 1 A7 3 D7
H   3 B8 2 A8 1 D8
H   4 B9 3 A9 2 D9
H   5 B10 4 A10 3 D10
H   5 B11 4 A11 3 D11
H   5 B12 4 A12 3 D12
Variables:
B1        1.33499
B2        1.47720
A2      121.15568
B3        1.34038
A3      120.89786
D3      180.00000
B4        1.49984
A4      121.91734
D4      180.00000
B5        1.08606
A5      121.19377
D5      360.00000
B6        1.08522
A6      119.97168
D6      180.00000
B7        1.08675
A7      118.93447
D7      180.00000
B8        1.08734
A8      119.20915
D8        0.00000
B9        1.08674
A9      120.09145
D9      360.00000
B10        1.11120
A10      111.98308
D10      360.00000
B11        1.10973
A11      109.23801
D11      120.40569
B12        1.10973
A12      109.23801
D12      239.59431

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

