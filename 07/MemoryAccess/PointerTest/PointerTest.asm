// {'instruction': 'push', 'argument': 'constant', 'value': '3030'}--> 7 lines
@3030
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
// {'instruction': 'push', 'argument': 'constant', 'value': '3040'}--> 7 lines
@3040
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
// {'instruction': 'push', 'argument': 'constant', 'value': '32'}--> 7 lines
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'this', 'value': '2'}--> 12 lines
@THIS
D=M
@2
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'constant', 'value': '46'}--> 7 lines
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'that', 'value': '6'}--> 12 lines
@THAT
D=M
@6
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// {'instruction': 'push', 'argument': 'pointer', 'value': '0'}--> 10 lines
@3
D=A
@0
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
// {'instruction': 'push', 'argument': 'pointer', 'value': '1'}--> 10 lines
@3
D=A
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
// {'instruction': 'push', 'argument': 'this', 'value': '2'}--> 10 lines
@2
D=A
@THIS
A=D+M
D=M
@R0
A=M
M=D
@R0
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
// {'instruction': 'push', 'argument': 'that', 'value': '6'}--> 10 lines
@6
D=A
@THAT
A=D+M
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
