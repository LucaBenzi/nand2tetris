// {'instruction': 'function', 'argument': 'Sys.init', 'value': '0'}--> 14 lines
(Sys.init)
@R14
M=0
// {'instruction': 'push', 'argument': 'constant', 'value': '6'}--> 7 lines
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '8'}--> 7 lines
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'call', 'argument': 'Class1.set', 'value': '2'}--> 50 lines
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
@2
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

@Class1.set
0;JEQ
(Sys.init$0)
// {'instruction': 'pop', 'argument': 'temp', 'value': '0'}--> 12 lines
@5
D=A
@0
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '23'}--> 7 lines
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '15'}--> 7 lines
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'call', 'argument': 'Class2.set', 'value': '2'}--> 50 lines
@Sys.init$1
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
@2
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

@Class2.set
0;JEQ
(Sys.init$1)
// {'instruction': 'pop', 'argument': 'temp', 'value': '0'}--> 12 lines
@5
D=A
@0
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// {'instruction': 'call', 'argument': 'Class1.get', 'value': '0'}--> 50 lines
@Sys.init$2
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
@0
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

@Class1.get
0;JEQ
(Sys.init$2)
// {'instruction': 'call', 'argument': 'Class2.get', 'value': '0'}--> 50 lines
@Sys.init$3
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
@0
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

@Class2.get
0;JEQ
(Sys.init$3)
// {'instruction': 'label', 'argument': 'WHILE'}--> 1 lines
(Sys.init$WHILE)
// {'instruction': 'goto', 'argument': 'WHILE'}--> 2 lines
@Sys.init$WHILE
0;JEQ
// {'instruction': 'function', 'argument': 'Class1.set', 'value': '0'}--> 14 lines
(Class1.set)
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
// {'instruction': 'pop', 'argument': 'static', 'value': '0'}--> 6 lines
// nuovo
@SP
M=M-1
A=M
D=M
@Class1.0
M=D

//  vecchio
// @16
// D=A
// @0
// D=A+D
// @R13
// M=D
// @SP
// AM=M-1
// D=M
// @R13
// A=M
// M=D
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
// {'instruction': 'pop', 'argument': 'static', 'value': '1'}--> 6 lines
// nuovo
@SP
M=M-1
A=M
D=M
@Class1.1
M=D

//  vecchio
// @16
// D=A
// @1
// D=A+D
// @R13
// M=D
// @SP
// AM=M-1
// D=M
// @R13
// A=M
// M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '0'}--> 7 lines
@0
D=A
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
// {'instruction': 'function', 'argument': 'Class1.get', 'value': '0'}--> 14 lines
(Class1.get)
@R14
M=0
// {'instruction': 'push', 'argument': 'static', 'value': '0'}--> 7 lines
// nuovo
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// @0
// D=A
// @16
// A=D+A
// D=M
// @SP
// A=M
// M=D
// @SP
// M=M+1
// {'instruction': 'push', 'argument': 'static', 'value': '1'}--> 7 lines
// nuovo
@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1

// @1
// D=A
// @16
// A=D+A
// D=M
// @SP
// A=M
// M=D
// @SP
// M=M+1
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
// {'instruction': 'function', 'argument': 'Class2.set', 'value': '0'}--> 14 lines
(Class2.set)
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
// {'instruction': 'pop', 'argument': 'static', 'value': '0'}--> 6 lines
// nuovo
@SP
M=M-1
A=M
D=M
@Class2.0
M=D

//  vecchio
// @16
// D=A
// @0
// D=A+D
// @R13
// M=D
// @SP
// AM=M-1
// D=M
// @R13
// A=M
// M=D
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
// {'instruction': 'pop', 'argument': 'static', 'value': '1'}--> 6 lines
// nuovo
@SP
M=M-1
A=M
D=M
@Class2.1
M=D

//  vecchio
// @16
// D=A
// @1
// D=A+D
// @R13
// M=D
// @SP
// AM=M-1
// D=M
// @R13
// A=M
// M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '0'}--> 7 lines
@0
D=A
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
// {'instruction': 'function', 'argument': 'Class2.get', 'value': '0'}--> 14 lines
(Class2.get)
@R14
M=0
// {'instruction': 'push', 'argument': 'static', 'value': '0'}--> 7 lines
// nuovo
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// @0
// D=A
// @16
// A=D+A
// D=M
// @SP
// A=M
// M=D
// @SP
// M=M+1
// {'instruction': 'push', 'argument': 'static', 'value': '1'}--> 7 lines
// nuovo
@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1

// @1
// D=A
// @16
// A=D+A
// D=M
// @SP
// A=M
// M=D
// @SP
// M=M+1
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
