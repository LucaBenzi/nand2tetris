// {'instruction': 'push', 'argument': 'constant', 'value': '7'}--> 7 lines
@7
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
// {'instruction': 'add'}--> 17 lines
@SP
M=M-1
// pop in D
@SP
A=M
D=M
// descrmento SP
@SP
M=M-1
// pop in M
@SP
A=M
// eseguo calcolo
M=D+M
// incremento SP
@SP
M=M+1
