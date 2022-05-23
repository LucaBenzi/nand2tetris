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
// push constant 3030
@0
@0
@0
@3030
D=A
@R0
A=M
M=D
@R0
M=M+1
// pop pointer 0
@3
D=A
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
// push constant 3040
@0
@0
@0
@3040
D=A
@R0
A=M
M=D
@R0
M=M+1
// pop pointer 1
@4
D=A
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
// push constant 32
@0
@0
@0
@32
D=A
@R0
A=M
M=D
@R0
M=M+1
// pop this 2
@R3
D=M
@2
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
// push constant 46
@0
@0
@0
@46
D=A
@R0
A=M
M=D
@R0
M=M+1
// pop that 6
@R4
D=M
@6
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
// push pointer 0
@0
@0
@0
@R3
D=M
@R0
A=M
M=D
@R0
M=M+1
// push pointer 1
@0
@0
@0
@R4
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
// push this 2
@2
D=A
@R3
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
// push that 6
@6
D=A
@R4
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
