// {'instruction': 'function', 'argument': 'Sys.init', 'value': '0'}--> 14 lines
(Sys.init)
@R14
M=0
// {'instruction': 'push', 'argument': 'constant', 'value': '4000'}--> 7 lines
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'pointer', 'value': '0'}--> 15 lines
@3
D=A
@0
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '5000'}--> 7 lines
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'pointer', 'value': '1'}--> 15 lines
@3
D=A
@1
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'call', 'argument': 'Sys.main', 'value': '0'}--> 50 lines
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

@Sys.main
0;JEQ
(Sys.init$0)
// {'instruction': 'pop', 'argument': 'temp', 'value': '1'}--> 12 lines
@5
D=A
@1
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// {'instruction': 'label', 'argument': 'LOOP'}--> 1 lines
(Sys.init$LOOP)
// {'instruction': 'goto', 'argument': 'LOOP'}--> 2 lines
@Sys.init$LOOP
0;JEQ
// {'instruction': 'function', 'argument': 'Sys.main', 'value': '5'}--> 14 lines
(Sys.main)
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
@LCL
D=M
@R14
A=M+D
M=0
@R14
M=M+1
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '4001'}--> 7 lines
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'pointer', 'value': '0'}--> 15 lines
@3
D=A
@0
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '5001'}--> 7 lines
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'pointer', 'value': '1'}--> 15 lines
@3
D=A
@1
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '200'}--> 7 lines
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'local', 'value': '1'}--> 15 lines
@LCL
D=M
@1
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '40'}--> 7 lines
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'local', 'value': '2'}--> 15 lines
@LCL
D=M
@2
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '6'}--> 7 lines
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'local', 'value': '3'}--> 15 lines
@LCL
D=M
@3
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '123'}--> 7 lines
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'call', 'argument': 'Sys.add12', 'value': '1'}--> 50 lines
@Sys.main$1
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

@Sys.add12
0;JEQ
(Sys.main$1)
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
// {'instruction': 'push', 'argument': 'local', 'value': '2'}--> 10 lines
@LCL
D=M
@2
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
// {'instruction': 'push', 'argument': 'local', 'value': '3'}--> 10 lines
@LCL
D=M
@3
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
// {'instruction': 'push', 'argument': 'local', 'value': '4'}--> 10 lines
@LCL
D=M
@4
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
// {'instruction': 'function', 'argument': 'Sys.add12', 'value': '0'}--> 14 lines
(Sys.add12)
@R14
M=0
// {'instruction': 'push', 'argument': 'constant', 'value': '4002'}--> 7 lines
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'pointer', 'value': '0'}--> 15 lines
@3
D=A
@0
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '5002'}--> 7 lines
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'pointer', 'value': '1'}--> 15 lines
@3
D=A
@1
A=D+A
D=A
@R13
M=D
@R0
M=M-1
@R0
A=M
D=M
@R13
A=M
M=D
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
// {'instruction': 'push', 'argument': 'constant', 'value': '12'}--> 7 lines
@12
D=A
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
