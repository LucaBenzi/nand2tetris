// {'instruction': 'function', 'argument': 'Sys.init', 'value': '0'}--> 14 lines
(Sys.init)
@R14
M=0
// {'instruction': 'push', 'argument': 'constant', 'value': '4'}--> 7 lines
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'call', 'argument': 'Main.fibonacci', 'value': '1'}--> 50 lines
@Sys.init$0
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
@1
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

@Main.fibonacci
0;JEQ
(Sys.init$0)
// {'instruction': 'label', 'argument': 'WHILE'}--> 1 lines
(Sys.init$WHILE)
// {'instruction': 'goto', 'argument': 'WHILE'}--> 2 lines
@Sys.init$WHILE
0;JEQ
// {'instruction': 'function', 'argument': 'Main.fibonacci', 'value': '0'}--> 14 lines
(Main.fibonacci)
@R14
M=0
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
@Main.fibonacci$IF_TRUE
D;JNE
// {'instruction': 'goto', 'argument': 'IF_FALSE'}--> 2 lines
@Main.fibonacci$IF_FALSE
0;JEQ
// {'instruction': 'label', 'argument': 'IF_TRUE'}--> 1 lines
(Main.fibonacci$IF_TRUE)
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
(Main.fibonacci$IF_FALSE)
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
// {'instruction': 'call', 'argument': 'Main.fibonacci', 'value': '1'}--> 50 lines
@Main.fibonacci$1
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
@1
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

@Main.fibonacci
0;JEQ
(Main.fibonacci$1)
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
// {'instruction': 'call', 'argument': 'Main.fibonacci', 'value': '1'}--> 50 lines
@Main.fibonacci$2
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
@1
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

@Main.fibonacci
0;JEQ
(Main.fibonacci$2)
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
