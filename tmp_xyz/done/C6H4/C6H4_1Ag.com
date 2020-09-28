%nosave
%nproc=8
%mem=2gb
%chk=input

#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 1
C  
C   1 B1
C   1 B2 2 A2
C   2 B3 1 A3 3 D3
H   1 B4 2 A4 3 D4
H   2 B5 1 A5 3 D5
C   2 B6 1 A6 3 D6
C   2 B7 1 A7 3 D7
H   2 B8 1 A8 3 D8
H   2 B9 1 A9 3 D9
Variables:
B1        1.34449
B2        1.42550
A2      122.81928
B3        1.42550
A3      122.81928
D3      180.00000
B4        1.08629
A4      119.52004
D4      180.00000
B5        1.08629
A5      119.52004
D5      360.00000
B6        3.54596
A6       38.59988
D6        0.00000
B7        2.63242
A7      122.81928
D7      180.00000
B8        4.56155
A8       42.84091
D8      360.00000
B9        3.69072
A9      122.81736
D9      180.00000

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read

