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
C   3 B3 2 A3 1 D3
H   3 B4 2 A4 1 D4
C   2 B5 1 A5 3 D5
H   2 B6 1 A6 3 D6
H   1 B7 2 A7 3 D7
H   1 B8 2 A8 3 D8
H   2 B9 1 A9 3 D9
Variables:
B1        1.33761
B2        1.50310
A2      120.42991
B3        1.48279
A3      118.20533
D3      231.63879
B4        1.11326
A4      118.95469
D4       53.51971
B5        3.65778
A5      137.10540
D5      311.65934
B6        4.66836
A6      137.44404
D6      304.71114
B7        1.08816
A7      120.98210
D7      181.24378
B8        1.08563
A8      120.74133
D8        0.10402
B9        1.08740
A9      119.12656
D9      177.97490

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P ROCCSD(T)/aug-cc-pvtz geom=allcheck guess=read

