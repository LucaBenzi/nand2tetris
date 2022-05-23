// {'instruction': 'push', 'argument': 'constant', 'value': '111'}--> 7 lines
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '333'}--> 7 lines
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '888'}--> 7 lines
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// {'instruction': 'pop', 'argument': 'static', 'value': '8'}--> 6 lines
// nuovo
@SP
M=M-1
D=M
@default.8
M=D
@SP



//  vecchio
// @16
// D=A
// @8
// D=A+D
// @R13
// M=D
// @SP
// AM=M-1
// D=M
// @R13
// A=M
// M=D
// {'instruction': 'pop', 'argument': 'static', 'value': '3'}--> 6 lines
// nuovo
@SP
M=M-1
D=M
@default.3
M=D
@SP



//  vecchio
// @16
// D=A
// @3
// D=A+D
// @R13
// M=D
// @SP
// AM=M-1
// D=M
// @R13
// A=M
// M=D
// {'instruction': 'pop', 'argument': 'static', 'value': '1'}--> 6 lines
// nuovo
@SP
M=M-1
D=M
@default.1
M=D
@SP



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
// {'instruction': 'push', 'argument': 'static', 'value': '3'}--> 7 lines
// nuovo
@default.3
D=M
@SP
A=M
M=D
@SP
M=M+1

// @3
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
@default.1
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
// {'instruction': 'push', 'argument': 'static', 'value': '8'}--> 7 lines
// nuovo
@default.8
D=M
@SP
A=M
M=D
@SP
M=M+1

// @8
// D=A
// @16
// A=D+A
// D=M
// @SP
// A=M
// M=D
// @SP
// M=M+1
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
