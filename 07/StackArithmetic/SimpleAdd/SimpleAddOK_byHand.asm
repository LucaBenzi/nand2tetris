// starting conditions
	@256
	D=A
	@R0
	M=D
	
// push constant 7
	@7
	D=A
	@R0
	A=M
	M=D
	@R0
	M=M+1	

//push constant 8
	@8
	D=A
	@R0
	A=M
	M=D
	// Incremento SP
	@R0
	M=M+1

//add
	// descrmento SP
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