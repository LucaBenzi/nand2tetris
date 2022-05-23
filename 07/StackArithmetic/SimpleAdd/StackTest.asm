@256
D=A
@R0
M=D
// push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// eq  
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
D=M-D
@TRUE0
D;JEQ
@FALSE0
0;JEQ
(TRUE0)
@R0
A=M
M=-1
@END_EQ0
0;JEQ
(FALSE0)
@R0
A=M
M=0
@END_EQ0
0;JEQ
(END_EQ0)
// incremento SP
@R0
M=M+1
// push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 16
@16
D=A
@0
A=M
M=D
@0
M=M+1
// eq  
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
D=M-D
@TRUE1
D;JEQ
@FALSE1
0;JEQ
(TRUE1)
@R0
A=M
M=-1
@END_EQ1
0;JEQ
(FALSE1)
@R0
A=M
M=0
@END_EQ1
0;JEQ
(END_EQ1)
// incremento SP
@R0
M=M+1
// push constant 16
@16
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// eq  
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
// incremento SP
@R0
M=M+1
// push constant 892
@892
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// lt  
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
D=M-D
@TRUE3
D;JLT
@FALSE3
0;JEQ
(TRUE3)
@R0
A=M
M=-1
@END_EQ3
0;JEQ
(FALSE3)
@R0
A=M
M=0
@END_EQ3
0;JEQ
(END_EQ3)
// incremento SP
@R0
M=M+1
// push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 892
@892
D=A
@0
A=M
M=D
@0
M=M+1
// lt  
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
D=M-D
@TRUE4
D;JLT
@FALSE4
0;JEQ
(TRUE4)
@R0
A=M
M=-1
@END_EQ4
0;JEQ
(FALSE4)
@R0
A=M
M=0
@END_EQ4
0;JEQ
(END_EQ4)
// incremento SP
@R0
M=M+1
// push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// lt  
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
D=M-D
@TRUE5
D;JLT
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
// incremento SP
@R0
M=M+1
// push constant 32767
@32767
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// gt  
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
D=M-D
@TRUE6
D;JGT
@FALSE6
0;JEQ
(TRUE6)
@R0
A=M
M=-1
@END_EQ6
0;JEQ
(FALSE6)
@R0
A=M
M=0
@END_EQ6
0;JEQ
(END_EQ6)
// incremento SP
@R0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 32767
@32767
D=A
@0
A=M
M=D
@0
M=M+1
// gt  
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
D=M-D
@TRUE7
D;JGT
@FALSE7
0;JEQ
(TRUE7)
@R0
A=M
M=-1
@END_EQ7
0;JEQ
(FALSE7)
@R0
A=M
M=0
@END_EQ7
0;JEQ
(END_EQ7)
// incremento SP
@R0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// gt  
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
D=M-D
@TRUE8
D;JGT
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
// incremento SP
@R0
M=M+1
// push constant 57
@57
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 31
@31
D=A
@0
A=M
M=D
@0
M=M+1
// push constant 53
@53
D=A
@0
A=M
M=D
@0
M=M+1
// add  
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
// push constant 112
@112
D=A
@0
A=M
M=D
@0
M=M+1
// sub  
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
// neg  
@R0
M=M-1
// pop in D
@R0
A=M
D=M
// eseguo calcolo
M=-D
// incremento SP
@R0
M=M+1
// and  
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
M=D&M
// incremento SP
@R0
M=M+1
// push constant 82
@82
D=A
@0
A=M
M=D
@0
M=M+1
// or  
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
M=D|M
// incremento SP
@R0
M=M+1
// not  
@R0
M=M-1
// pop in D
@R0
A=M
D=M
// eseguo calcolo
M=!D
// incremento SP
@R0
M=M+1
