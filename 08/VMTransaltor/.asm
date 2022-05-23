// {'instruction': 'function', 'argument': 'Sys.init', 'value': '0'}--> 14 lines
// Advanced instruction: see advanced instruction guide in static directory
[init]
(Sys.init)
"@R14"
"M=0"
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
// {'instruction': 'push', 'argument': 'constant', 'value': '4'}--> 7 lines
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'call', 'argument': 'Main.fibonacci', 'value': '1'}--> 0 lines
// {'instruction': 'label', 'argument': 'WHILE'}--> 1 lines
(WHILE)
// {'instruction': 'goto', 'argument': 'WHILE'}--> 2 lines
@WHILE
0;JEQ
// {'instruction': 'function', 'argument': 'Main.fibonacci', 'value': '0'}--> 14 lines
// Advanced instruction: see advanced instruction guide in static directory
[init]
(Main.fibonacci)
"@R14"
"M=0"
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
// {'instruction': 'push', 'argument': 'constant', 'value': '2'}--> 7 lines
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'lt'}--> 29 lines
@R0
M=M-1
@R0
A=M
D=M
@R0
M=M-1
@R0
A=M
D=M-D
@TRUE8
D;JLT
@FALSE8
0;JEQ
(TRUE8)
@R0
A=M
M=-1
@END_EQ8
0;JEQ
(FALSE8)
@R0
A=M
M=0
@END_EQ8
0;JEQ
(END_EQ8)
@R0
M=M+1
// {'instruction': 'if-goto', 'argument': 'IF_TRUE'}--> 6 lines
@SP
M=M-1
A=M
D=M
@IF_TRUE
D;JNE
// {'instruction': 'goto', 'argument': 'IF_FALSE'}--> 2 lines
@IF_FALSE
0;JEQ
// {'instruction': 'label', 'argument': 'IF_TRUE'}--> 1 lines
(IF_TRUE)
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
// {'instruction': 'label', 'argument': 'IF_FALSE'}--> 1 lines
(IF_FALSE)
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
// {'instruction': 'push', 'argument': 'constant', 'value': '2'}--> 7 lines
@2
D=A
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
// {'instruction': 'call', 'argument': 'Main.fibonacci', 'value': '1'}--> 0 lines
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
// {'instruction': 'push', 'argument': 'constant', 'value': '1'}--> 7 lines
@1
D=A
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
// {'instruction': 'call', 'argument': 'Main.fibonacci', 'value': '1'}--> 0 lines
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
