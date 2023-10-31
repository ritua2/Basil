model basic -ndm 2 -ndf 3
node 1 0.0 0.0
node 2 1.0 0.0
fix 1 1 1 1
fix 2 0 1 0
uniaxialMaterial Elastic 1 3000.0
element zeroLength 1 1 2 -mat 1 -dir 1
load 2 1000.0 0.0 0.0
analyze 1
