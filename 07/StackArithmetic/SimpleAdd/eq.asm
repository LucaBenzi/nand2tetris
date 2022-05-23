// starting conditions
	@256
	D=A
	@R0
	M=D

// push constant 17
	@17
	D=A
	@R0
	A=M
	M=D
	@R0
	M=M+1	

// push constant 17
	@17
	D=A
	@R0
	A=M
	M=D
	@R0
	M=M+1	


// EQ
    // decremento SP
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
    D=D-M
    @TRUE
    D;JEQ
    @FALSE
    0;JEQ

    
(TRUE)
    @R0
    A=M
    M=-1
    @END_EQ
    0;JMP


(FALSE)
    @R0
    A=M
    M=0
    @END_EQ
    0;JMP

(END_EQ)
    // incremento SP
    @R0
    M=M+1
