// {'instruction': 'push', 'argument': 'constant', 'value': '10'}--> 7 lines
// ok testata
@10
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
// {'instruction': 'push', 'argument': 'constant', 'value': '21'}--> 7 lines
// ok testata
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '22'}--> 7 lines
// ok testata
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'argument', 'value': '2'}--> 15 lines
@ARG
D=M
@2
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
// {'instruction': 'pop', 'argument': 'argument', 'value': '1'}--> 15 lines
@ARG
D=M
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
// {'instruction': 'push', 'argument': 'constant', 'value': '36'}--> 7 lines
// ok testata
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'this', 'value': '6'}--> 15 lines
// ok tested
@THIS
D=M
@6
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
// {'instruction': 'push', 'argument': 'constant', 'value': '42'}--> 7 lines
// ok testata
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '45'}--> 7 lines
// ok testata
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'that', 'value': '5'}--> 15 lines
// ok tested
@THAT
D=M
@5
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
// {'instruction': 'pop', 'argument': 'that', 'value': '2'}--> 15 lines
// ok tested
@THAT
D=M
@2
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
// {'instruction': 'push', 'argument': 'constant', 'value': '510'}--> 7 lines
// ok testata
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'temp', 'value': '6'}--> 12 lines
// ok tested
@5
D=A
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
// {'instruction': 'push', 'argument': 'that', 'value': '5'}--> 10 lines
// ok testata
@5
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
// {'instruction': 'push', 'argument': 'this', 'value': '6'}--> 10 lines
// ok testata
@6
D=A
@THIS
A=D+M
D=M
@R0
A=M
M=D
@R0
M=M+1
// {'instruction': 'push', 'argument': 'this', 'value': '6'}--> 10 lines
// ok testata
@6
D=A
@THIS
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
// {'instruction': 'push', 'argument': 'temp', 'value': '6'}--> 10 lines
@6
D=A
@5
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
