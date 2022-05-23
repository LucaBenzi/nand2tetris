// {'instruction': 'push', 'argument': 'constant', 'value': '17'}--> 7 lines
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '17'}--> 7 lines
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'eq'}--> 29 lines
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
@TRUE2
D;JEQ
@FALSE2
0;JEQ
(TRUE2)
@R0
A=M
M=-1
@END_EQ2
0;JEQ
(FALSE2)
@R0
A=M
M=0
@END_EQ2
0;JEQ
(END_EQ2)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '17'}--> 7 lines
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '16'}--> 7 lines
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'eq'}--> 29 lines
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
@TRUE5
D;JEQ
@FALSE5
0;JEQ
(TRUE5)
@R0
A=M
M=-1
@END_EQ5
0;JEQ
(FALSE5)
@R0
A=M
M=0
@END_EQ5
0;JEQ
(END_EQ5)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '16'}--> 7 lines
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '17'}--> 7 lines
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'eq'}--> 29 lines
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
D;JEQ
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
// {'instruction': 'push', 'argument': 'constant', 'value': '892'}--> 7 lines
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '891'}--> 7 lines
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
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
@TRUE11
D;JLT
@FALSE11
0;JEQ
(TRUE11)
@R0
A=M
M=-1
@END_EQ11
0;JEQ
(FALSE11)
@R0
A=M
M=0
@END_EQ11
0;JEQ
(END_EQ11)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '891'}--> 7 lines
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '892'}--> 7 lines
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
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
@TRUE14
D;JLT
@FALSE14
0;JEQ
(TRUE14)
@R0
A=M
M=-1
@END_EQ14
0;JEQ
(FALSE14)
@R0
A=M
M=0
@END_EQ14
0;JEQ
(END_EQ14)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '891'}--> 7 lines
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '891'}--> 7 lines
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
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
@TRUE17
D;JLT
@FALSE17
0;JEQ
(TRUE17)
@R0
A=M
M=-1
@END_EQ17
0;JEQ
(FALSE17)
@R0
A=M
M=0
@END_EQ17
0;JEQ
(END_EQ17)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '32767'}--> 7 lines
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '32766'}--> 7 lines
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'gt'}--> 29 lines
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
@TRUE20
D;JGT
@FALSE20
0;JEQ
(TRUE20)
@R0
A=M
M=-1
@END_EQ20
0;JEQ
(FALSE20)
@R0
A=M
M=0
@END_EQ20
0;JEQ
(END_EQ20)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '32766'}--> 7 lines
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '32767'}--> 7 lines
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'gt'}--> 29 lines
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
@TRUE23
D;JGT
@FALSE23
0;JEQ
(TRUE23)
@R0
A=M
M=-1
@END_EQ23
0;JEQ
(FALSE23)
@R0
A=M
M=0
@END_EQ23
0;JEQ
(END_EQ23)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '32766'}--> 7 lines
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '32766'}--> 7 lines
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'gt'}--> 29 lines
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
@TRUE26
D;JGT
@FALSE26
0;JEQ
(TRUE26)
@R0
A=M
M=-1
@END_EQ26
0;JEQ
(FALSE26)
@R0
A=M
M=0
@END_EQ26
0;JEQ
(END_EQ26)
@R0
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '57'}--> 7 lines
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '31'}--> 7 lines
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'push', 'argument': 'constant', 'value': '53'}--> 7 lines
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
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
// {'instruction': 'push', 'argument': 'constant', 'value': '112'}--> 7 lines
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
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
// {'instruction': 'neg'}--> 8 lines
@SP
M=M-1
@SP
A=M
D=M
M=-D
@SP
M=M+1
// {'instruction': 'and'}--> 12 lines
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D&M
@SP
M=M+1
// {'instruction': 'push', 'argument': 'constant', 'value': '82'}--> 7 lines
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// ok testata
// {'instruction': 'or'}--> 12 lines
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D|M
@SP
M=M+1
// {'instruction': 'not'}--> 8 lines
@SP
M=M-1
@SP
A=M
D=M
M=!D
@SP
M=M+1
