// Advanced instruction: see advanced instruction guide in static directory
[init]
([label])
@R14
M=0
[repeat]
@LCL
D=M
@R14
A=M+D
M=0
@R14
M=M+1
@SP
M=M+1