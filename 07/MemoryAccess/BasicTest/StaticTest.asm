// prepare SP
@256
D=A
@R0
M=D
// prepare LCL
@300
D=A
@R1
M=D
// prepare ARG
@400
D=A
@R2
M=D
// prepare THIS
@3000
D=A
@R3
M=D
// prepare THAT
@3010
D=A
@R4
M=D
// push constant 111
@0
@0
@0
@111
D=A
@R0
A=M
M=D
@R0
M=M+1
// push constant 333
@0
@0
@0
@333
D=A
@R0
A=M
M=D
@R0
M=M+1
// push constant 888
@0
@0
@0
@888
D=A
@R0
A=M
M=D
@R0
M=M+1
// pop static 8
@16
D=M
@8
D=D+A
@R13
M=D
// descrmento SP
@R0
M=M-1
// pop in D
@R0
A=M
D=M
@R13
A=M
M=D
// pop static 3
@16
D=M
@3
D=D+A
@R13
M=D
// descrmento SP
@R0
M=M-1
// pop in D
@R0
A=M
D=M
@R13
A=M
M=D
// pop static 1
@16
D=M
@1
D=D+A
@R13
M=D
// descrmento SP
@R0
M=M-1
// pop in D
@R0
A=M
D=M
@R13
A=M
M=D
// push static 3
@3
D=A
@16
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
// push static 1
@1
D=A
@16
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
// sub  
@R0
M=M-1
// pop in D
@R0
A=M
D=M
// descrmento SP
@R0
M=M-1
// pop in M
@R0
A=M
// eseguo calcolo
M=M-D
// incremento SP
@R0
M=M+1
// push static 8
@8
D=A
@16
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
// add  
@R0
M=M-1
// pop in D
@R0
A=M
D=M
// descrmento SP
@R0
M=M-1
// pop in M
@R0
A=M
// eseguo calcolo
M=D+M
// incremento SP
@R0
M=M+1
