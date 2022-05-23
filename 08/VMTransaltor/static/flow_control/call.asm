@[return_address]
D=A
@R0
A=M
M=D
@R0
M=M+1
// save registers content "LCL", "ARG", "THIS", "THAT"
@LCL
D=M
@R0
A=M
M=D
@R0
M=M+1
@ARG
D=M
@R0
A=M
M=D
@R0
M=M+1
@THIS
D=M
@R0
A=M
M=D
@R0
M=M+1
@THAT
D=M
@R0
A=M
M=D
@R0
M=M+1

// ARG = SP-5-nArgs
@5
D=A
@[value]
D=D+A
@SP
D=M-D
@ARG
M=D

// LCL = SP
@SP
D=M
@LCL
M=D

@[label]
0;JEQ
([return_address])