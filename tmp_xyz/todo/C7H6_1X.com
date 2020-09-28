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
H   3 B4 2 A4 1 D4
C   2 B5 1 A5 3 D5
H   2 B6 1 A6 3 D6
H   1 B7 2 A7 3 D7
H   1 B8 2 A8 3 D8
C   3 B9 2 A9 1 D9
H   1 B10 2 A10 3 D10
C   3 B11 2 A11 1 D11
H   10 B12 3 A12 2 D12
Variables:
B1        2.66819
B2        2.42478
A2      154.50715
B3        1.44161
A3      150.15731
D3      186.79476
B4        1.08677
A4       90.64634
D4        5.30131
B5        4.89498
A5      170.05657
D5      348.36607
B6        5.91966
A6      172.62259
D6      340.50739
B7        1.10983
A7      107.10274
D7      181.22715
B8        1.10969
A8      107.31757
D8       92.13383
B9        1.33636
A9       30.39247
D9      184.87544
B10        1.10906
A10      117.19455
D10      316.43348
B11        3.54672
A11        8.62665
D11        1.47257
B12        1.08605
A12      120.31993
D12      179.27114

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

