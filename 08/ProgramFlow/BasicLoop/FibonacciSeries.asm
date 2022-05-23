//INSTRUCTION: {'command': 'push', 'segment': 'argument', 'value': '1'}
@1
D=A
@R2
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'pop', 'segment': 'pointer', 'value': '1'}
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
//INSTRUCTION: {'command': 'push', 'segment': 'constant', 'value': '0'}
@0
@0
@0
@0
D=A
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'pop', 'segment': 'that', 'value': '0'}
@R4
D=M
@0
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
//INSTRUCTION: {'command': 'push', 'segment': 'constant', 'value': '1'}
@0
@0
@0
@1
D=A
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'pop', 'segment': 'that', 'value': '1'}
@R4
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
//INSTRUCTION: {'command': 'push', 'segment': 'argument', 'value': '0'}
@0
D=A
@R2
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'push', 'segment': 'constant', 'value': '2'}
@0
@0
@0
@2
D=A
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'sub', 'segment': '', 'value': ''}
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
//INSTRUCTION: {'command': 'pop', 'segment': 'argument', 'value': '0'}
@R2
D=M
@0
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
//INSTRUCTION: {'command': 'label', 'location': 'MAIN_LOOP_START'}
(MAIN_LOOP_START)
//INSTRUCTION: {'command': 'push', 'segment': 'argument', 'value': '0'}
@0
D=A
@R2
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'if-goto', 'location': 'COMPUTE_ELEMENT'}
@R0
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
//INSTRUCTION: {'command': 'goto', 'location': 'END_PROGRAM'}
@R0
A=M
M=M-1
@END_PROGRAM
0;JEQ
//INSTRUCTION: {'command': 'label', 'location': 'COMPUTE_ELEMENT'}
(COMPUTE_ELEMENT)
//INSTRUCTION: {'command': 'push', 'segment': 'that', 'value': '0'}
@0
D=A
@R4
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'push', 'segment': 'that', 'value': '1'}
@1
D=A
@R4
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'add', 'segment': '', 'value': ''}
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
//INSTRUCTION: {'command': 'pop', 'segment': 'that', 'value': '2'}
@R4
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
//INSTRUCTION: {'command': 'push', 'segment': 'pointer', 'value': '1'}
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
//INSTRUCTION: {'command': 'push', 'segment': 'constant', 'value': '1'}
@0
@0
@0
@1
D=A
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'add', 'segment': '', 'value': ''}
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
//INSTRUCTION: {'command': 'pop', 'segment': 'pointer', 'value': '1'}
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
//INSTRUCTION: {'command': 'push', 'segment': 'argument', 'value': '0'}
@0
D=A
@R2
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'push', 'segment': 'constant', 'value': '1'}
@0
@0
@0
@1
D=A
@R0
A=M
M=D
@R0
M=M+1
//INSTRUCTION: {'command': 'sub', 'segment': '', 'value': ''}
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
//INSTRUCTION: {'command': 'pop', 'segment': 'argument', 'value': '0'}
@R2
D=M
@0
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
//INSTRUCTION: {'command': 'goto', 'location': 'MAIN_LOOP_START'}
@R0
A=M
M=M-1
@MAIN_LOOP_START
0;JEQ
//INSTRUCTION: {'command': 'label', 'location': 'END_PROGRAM'}
(END_PROGRAM)
