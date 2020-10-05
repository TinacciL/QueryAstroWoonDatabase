%nosave
%nproc=8
%mem=2gb
%chk=input
#P M062X/cc-pvtz nosymm opt(noeigentest) optcyc=120 freq

 Title

0 2
C          0.00000        0.00000       -0.02484
C          0.00000        0.00000        1.23225
C          0.00000        0.00000        2.56687
C          0.00000        0.00000        3.78001
H          0.00000        0.00000        4.84377
C          0.00000        0.00000       -1.33529

--Link1-- 
%nosave
%nproc=8
%mem=2500mb
%chk=input

#P CCSD(T)/aug-cc-pvtz geom=allcheck guess=read SCF(maxcyc=500) SCF=QC


