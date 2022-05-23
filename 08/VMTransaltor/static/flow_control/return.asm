//returnAddress = *(LCL-5)
@LCL
D=M
@5
A=D-A
D=M
@R15
M=D

//*ARG = pop()
@SP
AM=M-1
D=M
@ARG
A=M
M=D

//SP = ARG+1
@ARG
D=M+1
@SP
M=D

//THAT = *(LCL-1)
@LCL
A=M-1
D=M
@THAT
M=D

//THIS = *(LCL-2)
@LCL
D=M
@2
A=D-A
D=M
@THIS
M=D

//ARG = *(LCL-3)
@LCL
D=M
@3
A=D-A
D=M
@ARG
M=D

//LCL = *(LCL-4)
@LCL
D=M
@4
A=D-A
D=M
@LCL
M=D

// goto return address
@R15
A=M
0;JEQ