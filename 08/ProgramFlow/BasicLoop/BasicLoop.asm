// {'instruction': 'push', 'argument': 'constant', 'value': '0'}--> 7 lines
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'local', 'value': '0'}--> 15 lines
@LCL
D=M
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
// {'instruction': 'label', 'argument': 'LOOP_START'}--> 1 lines
(LOOP_START)
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
// {'instruction': 'pop', 'argument': 'local', 'value': '0'}--> 15 lines
@LCL
D=M
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
// {'instruction': 'pop', 'argument': 'argument', 'value': '0'}--> 15 lines
@ARG
D=M
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
// {'instruction': 'if-goto', 'argument': 'LOOP_START'}--> 6 lines
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JNE
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