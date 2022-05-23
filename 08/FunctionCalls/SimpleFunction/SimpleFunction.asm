// {'instruction': 'function', 'argument': 'SimpleFunction.test', 'value': '2'}--> 14 lines
(SimpleFunction.test)
@R14
M=0
@LCL
D=M
@R14
A=M+D
M=0
@R14
M=M+1
@SP
M=M+1
@LCL
D=M
@R14
A=M+D
M=0
@R14
M=M+1
@SP
M=M+1
// {'instruction': 'push', 'argument': 'local', 'value': '0'}--> 10 lines
@LCL
D=M
@0
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
// {'instruction': 'push', 'argument': 'local', 'value': '1'}--> 10 lines
@LCL
D=M
@1
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
// {'instruction': 'add'}--> 12 lines
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D+M
@SP
M=M+1
// {'instruction': 'not'}--> 8 lines
@SP
M=M-1
@SP
A=M
D=M
M=!D
@SP
M=M+1
// {'instruction': 'push', 'argument': 'argument', 'value': '0'}--> 10 lines
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'add'}--> 12 lines
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D+M
@SP
M=M+1
// {'instruction': 'push', 'argument': 'argument', 'value': '1'}--> 10 lines
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'sub'}--> 12 lines
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1
// {'instruction': 'return'}--> 46 lines
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
